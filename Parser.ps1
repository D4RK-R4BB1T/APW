function Export-ByKeywordAndColumn {
    param(
        [string]$inputFile,
        [string]$outputFileType
    )

    # Read the file based on its format
    $data = switch ($inputFile.Split('.')[-1]) {
        "csv"  { Import-Csv -Path $inputFile }
        "json" { Get-Content -Path $inputFile | ConvertFrom-Json }
        "txt"  { Get-Content -Path $inputFile }
        default { throw "Unsupported file format." }
    }

    $columns = $data | Get-Member -MemberType Properties | Select-Object -ExpandProperty Name
    $selectedColumns = $columns | Out-GridView -Title "Select columns" -OutputMode Multiple

    if ($outputFileType -eq "csv") {
        $keyword = Read-Host "Enter the keyword to filter by"

        # Filter data based on selected columns and keyword
        $filteredData = $data | Where-Object {
            $match = $false
            foreach ($column in $selectedColumns) {
                if ($_.($column) -eq $keyword) {
                    $match = $true
                    break
                }
            }
            $match
        }
    } elseif ($outputFileType -eq "json" -or $outputFileType -eq "txt") {
        $keyword = Read-Host "Enter the keyword to filter by"

        # Filter data based on keyword
        $filteredData = $data | Where-Object { $_ -match $keyword }
    } else {
        Write-Host "Invalid output file format!"
        return
    }

    $saveFileDialog = New-Object System.Windows.Forms.SaveFileDialog
    $saveFileDialog.Filter = "Files|*.$outputFileType"
    $saveFileDialog.FileName = "output.$outputFileType"
    $saveFileDialog.Title = "Select a location to save the $outputFileType file"

    $result = $saveFileDialog.ShowDialog()

    if ($result -eq 'OK') {
        $outputPath = $saveFileDialog.FileName

        switch ($outputFileType) {
            "csv" {
                $filteredData | Export-Csv -Path $outputPath -NoTypeInformation
                Write-Host "Filtered data saved to: $outputPath"
                break
            }
            "json" {
                $filteredData | ConvertTo-Json | Out-File -FilePath $outputPath
                Write-Host "Filtered data saved to: $outputPath"
                break
            }
            "txt" {
                $filteredData | Out-File -FilePath $outputPath
                Write-Host "Filtered data saved to: $outputPath"
                break
            }
            default {
                Write-Host "Invalid output file format!"
                break
            }
        }
    } else {
        Write-Host "Export cancelled."
    }
}

# Main script
$openFileDialog = New-Object System.Windows.Forms.OpenFileDialog
$openFileDialog.Filter = "Files|*.csv;*.json;*.txt"
$openFileDialog.Multiselect = $false

if ($openFileDialog.ShowDialog() -eq 'OK') {
    $selectedFile = $openFileDialog.FileName

    Write-Host "Choose an option:"
    Write-Host "1. Export to CSV"
    Write-Host "2. Export to JSON"
    Write-Host "3. Export to TXT"

    $choice = Read-Host "Enter your choice"

    switch ($choice) {
        "1" {
            Export-ByKeywordAndColumn -inputFile $selectedFile -outputFileType "csv"
            break
        }
        "2" {
            Export-ByKeywordAndColumn -inputFile $selectedFile -outputFileType "json"
            break
        }
        "3" {
            Export-ByKeywordAndColumn -inputFile $selectedFile -outputFileType "txt"
            break
        }
        default {
            Write-Host "Invalid choice. Please enter a valid option."
            break
        }
    }
} else {
    Write-Host "File selection cancelled."
}

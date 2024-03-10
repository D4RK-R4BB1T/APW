# Prompt user to enter the path for the input file
$inputFilePath = Read-Host "Enter the full path to the input text file (e.g., C:\Path\To\Your\Input\File.txt)"

# Check if the input file exists
if (Test-Path $inputFilePath -PathType Leaf) {
    # Prompt user to enter the path for the output file
    $outputFilePath = Read-Host "Enter the full path for the output text file (e.g., C:\Path\To\Your\Output\File.txt)"

    # Remove duplicates from the content
    $uniqueContent = Get-Content $inputFilePath | Select-Object -Unique

    # Save the unique content to the output file
    $uniqueContent | Out-File -FilePath $outputFilePath -Force

    Write-Host "Duplicates removed. Result saved to: $outputFilePath"
} else {
    Write-Host "Input file not found: $inputFilePath"
}

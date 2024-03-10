# Prompt user to enter the input file path
$inputFilePath = Read-Host "Enter the full path to the input file (e.g., C:\Path\To\Your\Input\File.txt)"

# Prompt user to enter the output file path
$outputFilePath = Read-Host "Enter the full path for the output file (e.g., C:\Path\To\Your\Output\File.txt)"

# Initialize a counter for the line number
$lineNumber = 1

# Create an array to store commands
$commands = @()

# Loop through each line in the input file
foreach ($line in Get-Content $inputFilePath) {
    # Create the command with the line content and line number
    $command = "sudo lynx -dump `"$line`" | awk '/http/{print `$2}' | uniq -u > $($lineNumber).txt &&"

    # Add the command to the array
    $commands += $command

    # Increment the line number counter
    $lineNumber++
}

# Save the commands to the output file
$commands | Out-File -FilePath $outputFilePath

Write-Host "Commands have been exported to $outputFilePath"

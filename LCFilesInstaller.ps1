$WarningPreference = 'SilentlyContinue'
$VersionFile = iwr -Uri "https://launcherupdates.lunarclientcdn.com/latest.yml" -OutFile "$env:Temp\Version.txt"
$Version = cat "$env:Temp\Version.txt" | Select-Object -First 1
$Version = $Version.Trim("version: ")
$GameVersion = $args[0]
$params = @{
  "hwid"="0";
  "hwid_private"="0";
  "os"="win32";
  "arch"="x64";
  "launcher_version"="$Version";
  "version"="$GameVersion";
  "branch"="master";
  "launch_type"="0";
  "classifier"="0";
}
$Index = iwr "https://api.lunarclientprod.com/launcher/launch" -Method POST -Body ($params|ConvertTo-Json) -ContentType "application/json" -OutFile "$env:Temp\Index.txt"
$Index = cat "$env:Temp\index.txt"
$Files=($Index | ConvertFrom-Json).launchTypeData.artifacts
$Licenses=($Index | ConvertFrom-Json).licenses
$JRE=($Index | ConvertFrom-Json).jre.download.url
$JRE_Name=($Index | ConvertFrom-Json).jre.executablePathInArchive[0]

$null = New-Item -Path ".lunarclient_files" -ItemType "Directory"
$null = New-Item -Path ".lunarclient_files\licenses" -Type "Directory"
$null = New-Item -Path ".lunarclient_files\offline\$GameVersion" -Type "Directory"
$null = New-Item -Path ".lunarclient_files\jre" -Type "Directory"
cls

Write-Output "Getting Licenses..."
foreach ($file in $Licenses) {
  curl.exe -# -L -o ".lunarclient_files\licenses\$($file.file)" $file.url
}
Write-Output "Downloading LC ($GameVersion)..."
Write-Output "Getting LC Jars, Natives & Optifine..."
foreach ($file in $Files) {
  if ($file.name.EndsWith(".jar")) {
    curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\$($file.name)" $file.url
  }
  if ($file.name.EndsWith(".zip")) {
    curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\$($file.name)" $file.url
    Expand-Archive -Path ".lunarclient_files\offline\$GameVersion\$($file.name)" -DestinationPath ".lunarclient_files\offline\$GameVersion\natives" -Force
  }
}

if (!(Test-Path -LiteralPath ".lunarclient_files\jre\$JRE_Name")){
Remove-Item -Path ".lunarclient_files\jre" -Force -Recurse | Out-Null
Write-Output "Downloading JRE..."
$null = New-Item -Path ".lunarclient_files\jre\$JRE_Name" -Type "Directory"
curl.exe -# -L -o "$env:Temp\$JRE_Name.zip" $JRE
Expand-Archive -Path "$env:Temp\$JRE_Name.zip" -DestinationPath ".lunarclient_files\jre" -Force
}

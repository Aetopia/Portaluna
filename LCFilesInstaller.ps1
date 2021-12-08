$VersionFile = iwr -Uri "https://launcherupdates.lunarclientcdn.com/latest.yml" -OutFile "$env:Temp\Version.txt"
$Version = cat "$env:Temp\Version.txt" | Select-Object -First 1
$Version = $Version.Trim("version: ")
$GameVersion = $args[0]
$params = @{
  "hwid"=""
  "os"="win32";
  "arch"="x64";
  "launcher_version"="$Version";
  "version"="$GameVersion";
  "branch"="master";
  "launch_type"="ONLINE";
  "classifier"="";
}
$Index = iwr "https://api.lunarclientprod.com/launcher/launch" -Method POST -Body ($params|ConvertTo-Json) -ContentType "application/json"
$Files=($Index.Content | ConvertFrom-Json).launchTypeData.artifacts
$Licenses=($Index.Content | ConvertFrom-Json).licenses

$null = New-Item -Path ".lunarclient_files" -ItemType "Directory" | Out-Null
$null = New-Item -Path ".lunarclient_files\licenses" -Type "Directory" | Out-Null
$null = New-Item -Path ".lunarclient_files\offline\$GameVersion" -Type "Directory" | Out-Null
cls

Write-Output "Getting Licenses..."
curl.exe -# -L -o ".lunarclient_files\licenses\ReplayMod.md" $Licenses[0].url
curl.exe -# -L -o ".lunarclient_files\licenses\Blur.md" $Licenses[1].url
Write-Output "Downloading LC ($GameVersion)..."
Write-Output "Getting LC Jars..."
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\vpatcher-prod.jar" $Files[0].url
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\lunar-prod-optifine.jar" $Files[1].url
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\lunar-libs.jar" $Files[2].url
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\lunar-assets-prod-1-optifine.jar" $Files[3].url
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\lunar-assets-prod-2-optifine.jar" $Files[4].url
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\lunar-assets-prod-3-optifine.jar" $Files[5].url
Write-Output "Getting Natives..."
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\natives-win-x64.zip" $Files[6].url
Expand-Archive -Path ".lunarclient_files\offline\$GameVersion\natives-win-x64.zip" -DestinationPath ".lunarclient_files\offline\$GameVersion\natives" -Force | Out-Null
Write-Output "Getting OptiFine..."
curl.exe -# -L -o ".lunarclient_files\offline\$GameVersion\OptiFine.jar" $Files[7].url


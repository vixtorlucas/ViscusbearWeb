$projectRoot = $PSScriptRoot
$cursor = Get-Item -LiteralPath $projectRoot
$runtimeRoot = $null

while ($null -ne $cursor) {
  $candidateRoot = Join-Path $cursor.FullName "tools\Ruby33-x64\msys64"
  $candidateRuby = Join-Path $candidateRoot "ucrt64\bin\ruby.exe"

  if (Test-Path -LiteralPath $candidateRuby) {
    $runtimeRoot = $candidateRoot
    break
  }

  $cursor = $cursor.Parent
}

if ($null -eq $runtimeRoot) {
  $installedRuntime = "C:\Users\victo\Documents\Codex\tools\Ruby33-x64\msys64"
  if (Test-Path -LiteralPath (Join-Path $installedRuntime "ucrt64\bin\ruby.exe")) {
    $runtimeRoot = $installedRuntime
  } else {
    throw "Ruby 3.3 não foi encontrado na pasta tools do workspace."
  }
}

$usedDrives = (Get-PSDrive -PSProvider FileSystem).Name
$freeDrives = @("R", "S", "T", "U", "V", "W", "X", "Y", "Z") | Where-Object { $_ -notin $usedDrives }

if ($freeDrives.Count -lt 2) {
  throw "Não há duas letras de unidade livres para iniciar o ambiente local."
}

$runtimeDrive = "$($freeDrives[0]):"
$projectDrive = "$($freeDrives[1]):"
$ucrtRoot = Join-Path $runtimeRoot "ucrt64"

subst.exe $runtimeDrive $ucrtRoot
subst.exe $projectDrive $projectRoot

try {
  $rubyBin = "$runtimeDrive\bin"
  $msysBin = Join-Path $runtimeRoot "usr\bin"
  $env:Path = "$rubyBin;$msysBin;$env:Path"
  $env:SSL_CERT_FILE = "$runtimeDrive\etc\ssl\cert.pem"
  $env:BUNDLE_USER_CACHE = Join-Path (Split-Path $runtimeRoot -Parent) "bundle-cache"

  Set-Location "$projectDrive\"
  Write-Host "Viscusbear disponível em http://localhost:4000"
  Write-Host "Use Ctrl+C para encerrar."
  & (Join-Path $rubyBin "jekyll.bat") serve --livereload --host 127.0.0.1 --port 4000
} finally {
  Set-Location -LiteralPath $projectRoot
  subst.exe $projectDrive /D
  subst.exe $runtimeDrive /D
}

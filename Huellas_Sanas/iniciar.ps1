param(
    [string]$Direccion = '127.0.0.1:8000'
)

$ErrorActionPreference = 'Stop'
$pythonLocal = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $pythonLocal)) {
    Write-Error 'No encuentro .venv. Crea el entorno e instala Django antes de iniciar.'
    exit 1
}

Push-Location $PSScriptRoot
try {
    & $pythonLocal manage.py migrate
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    & $pythonLocal manage.py cargar_datos_demo
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    & $pythonLocal manage.py runserver $Direccion
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}

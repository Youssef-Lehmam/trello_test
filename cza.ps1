if (Get-Process -Name "spoolsv") {
    Write-Output "est en cours d'exécution."
} else {
    Write-Output "n'est pas en cours d'exécution."
}

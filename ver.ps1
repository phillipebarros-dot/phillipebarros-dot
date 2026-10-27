# Tira um print de um SVG de assets/ com o Edge headless. Uso: ver.ps1 header 1200 400 saida.png
param($nome, $w, $h, $saida)
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if (!(Test-Path $edge)) { $edge = "C:\Program Files\Microsoft\Edge\Application\msedge.exe" }
$html = Join-Path $env:TEMP "ver_$nome.html"
[IO.File]::WriteAllText($html, "<html><body style='margin:0;background:#0d1117'><img src='file:///D:/projetos/perfil-github/assets/$nome.svg' width='$w'></body></html>")
if (Test-Path $saida) { Remove-Item $saida }
$p = Start-Process $edge -ArgumentList @('--headless=new', '--disable-gpu', '--hide-scrollbars', "--window-size=$w,$h", "--screenshot=$saida", "file:///$($html -replace '\\','/')") -PassThru -WindowStyle Hidden
$p | Wait-Process -Timeout 25 -ErrorAction SilentlyContinue
if (!$p.HasExited) { $p | Stop-Process -Force }
Test-Path $saida

# Ping Sweeper (PowerShell, Windows)
# Tarmoqdagi "tirik" hostlarni topadi va alive_hosts.txt ga saqlaydi.
# Faqat o'zingizning yoki ruxsat berilgan tarmoqda ishlating!

$outputFile = "alive_hosts.txt"

# 1) Foydalanuvchidan tarmoq prefiksini qabul qilish
$prefix = Read-Host "Tarmoq prefiksini kiriting (masalan, 192.168.1)"

# Format tekshiruvi: uchta oktet bo'lishi kerak
if ($prefix -notmatch '^(\d{1,3}\.){2}\d{1,3}$') {
    Write-Host "Xato: format noto'g'ri. Masalan: 192.168.1" -ForegroundColor Red
    exit 1
}

Write-Host "Skanerlanmoqda: $prefix.1 - $prefix.255 ..."

# 2) Barcha 255 ta pingni BIR VAQTDA fon rejimida yuboramiz (asinxron)
$jobs = New-Object System.Collections.Generic.List[object]

for ($i = 1; $i -le 255; $i++) {
    $ip = "$prefix.$i"
    $pinger = New-Object System.Net.NetworkInformation.Ping
    $task = $pinger.SendPingAsync($ip, 1000)   # 1000 ms kutish
    $jobs.Add([PSCustomObject]@{ IP = $ip; Task = $task })
}

# 3) Natijalarni yig'amiz: faqat javob berganlar
$aliveHosts = @()

foreach ($job in $jobs) {
    try {
        if ($job.Task.Result.Status -eq "Success") {
            $aliveHosts += $job.IP
        }
    }
    catch {
        # xato bo'lgan IP ni o'tkazib yuboramiz (ekranga chiqarmaymiz)
    }
}

# 4) Faqat tirik hostlarni ekranga chiqarish
Write-Host ""
Write-Host "Tirik hostlar:" -ForegroundColor Green
foreach ($h in $aliveHosts) {
    Write-Host $h
}

# 5) Faylga saqlash
$aliveHosts | Out-File $outputFile -Encoding ascii

Write-Host ""
Write-Host "Jami topildi: $($aliveHosts.Count) ta host"
Write-Host "Natijalar $outputFile fayliga saqlandi."

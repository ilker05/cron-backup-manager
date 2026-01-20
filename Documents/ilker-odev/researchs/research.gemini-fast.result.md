# Cronjobs & Backup Scripts: Teknik Araştırma Raporu

## 1. Temel Çalışma Prensipleri
Cron, Unix benzeri işletim sistemlerinde zaman tabanlı bir iş zamanlayıcıdır (job scheduler).
- **Daemon:** Arka planda sürekli çalışan `crond` servisi, her dakika yapılandırma dosyalarını (`crontab`) kontrol eder.
- **Zamanlama Sözdizimi:** 5 yıldız formatı kullanılır: `dakika saat gün ay haftanın_günü komut`.
- **Otomasyon:** Yedekleme scriptleri (Python, Bash) bu zamanlayıcı sayesinde insan müdahalesi olmadan çalışır.

## 2. Best Practices (En İyi Uygulama Yöntemleri)
- **Loglama:** Her cron işinin çıktısı mutlaka loglanmalıdır (`>> /var/log/myjob.log 2>&1`). Sessiz hatalar en büyük risktir.
- **Mutlak Yollar (Absolute Paths):** Komutlarda `python` yerine `/usr/bin/python3` gibi tam yol kullanılmalıdır.
- **Atomik Yedekleme:** Yedekleme yaparken dosya bozulmasını önlemek için önce geçici bir dosyaya yazıp işlem bitince adını değiştirmek (rename) önerilir.
- **Hata Yönetimi:** Script içinde `try-except` blokları ile hatalar yakalanmalı ve gerekirse e-posta/webhook ile bildirim gönderilmelidir.

## 3. Benzer Açık Kaynak Projeler
Kendi aracımıza alternatif olabilecek popüler araçlar:
- **Cronicle:** Görsel bir arayüze sahip cron yönetim aracı.
- **Rundeck:** Daha karmaşık iş akışları ve otomasyonlar için kullanılan kurumsal bir araç.
- **BorgBackup:** Veri tekilleştirme (deduplication) özelliğine sahip gelişmiş yedekleme aracı.
- **Healthchecks.io:** Cron işlerinin çalışıp çalışmadığını dışarıdan (ping atarak) izleyen servis.

## 4. Kritik Yapılandırma Dosyaları
- `/etc/crontab`: Sistem geneli zamanlanmış görevler.
- `/var/spool/cron/`: Kullanıcılara özel crontab dosyalarının tutulduğu dizin.
- `/etc/cron.d/`: Paketlerin kendi cron dosyalarını bıraktığı dizin.
- `/etc/cron.daily`, `/etc/cron.weekly`: Belirli aralıklarla çalışacak scriptlerin direkt atıldığı klasörler.

## 5. Güvenlik Kritik Noktaları
- **Yetki (Privilege):** Cron işleri mümkünse `root` olarak **çalıştırılmamalıdır**. En az yetkiye sahip (Least Privilege) özel bir kullanıcı ile çalıştırılmalıdır.
- **Dosya İzinleri:** Crontab tarafından çağrılan script dosyaları sadece sahibi tarafından yazılabilir (`chmod 700` veya `750`) olmalıdır. Aksi takdirde "Privilege Escalation" saldırılarına açık hale gelir.
- **Hassas Veriler:** Veritabanı şifreleri script içine gömülmemeli, ortam değişkenlerinden (Environment Variables) veya güvenli config dosyalarından okunmalıdır.

## 6. Web Page Generation (Özet HTML)
```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Cron & Backup Araştırma Özeti</title>
    <style>
        body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; }
        .card { border: 1px solid #ddd; padding: 15px; margin-bottom: 20px; border-radius: 8px; }
        .highlight { background-color: #f0f8ff; padding: 5px; font-family: monospace; }
    </style>
</head>
<body>
    <h1>Cronjobs & Backup Scripts Özeti</h1>
    
    <div class="card">
        <h3>🚀 Temel Prensip</h3>
        <p>Cron, zaman tabanlı bir görev yöneticisidir. Format: <span class="highlight">* * * * * komut</span></p>
    </div>

    <div class="card">
        <h3>🛡️ Güvenlik İpuçları</h3>
        <ul>
            <li>Root kullanmaktan kaçının.</li>
            <li>Script dosyalarına yazma iznini (write permission) kısıtlayın.</li>
            <li>Mutlaka log tutun.</li>
        </ul>
    </div>
</body>
</html>
```

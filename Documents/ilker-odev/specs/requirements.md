# Proje Gereksinim Analizi (Specs)

## 1. Proje Tanımı
Kullanıcıların karmaşık Cron zamanlamalarını yönetebileceği, otomatik yedekleme yapabileceği ve sistem loglarını izleyebileceği bir arayüz aracıdır.

## 2. Fonksiyonel Gereksinimler
- **Cron Çevirici (Translator):** - `*/5 * * * *` gibi ifadeleri insan diline (Örn: "Her 5 dakikada bir") çevirmelidir.
  - `cron-descriptor` kütüphanesi kullanılmalıdır.
- **Yedekleme Sihirbazı (Backup Wizard):**
  - Kullanıcı kaynak ve hedef klasör seçebilmelidir.
  - İşlem sonucunda `.zip` formatında arşiv oluşturulmalıdır.
  - Hatalı dosya yolları için kullanıcı uyarılmalıdır.
- **Log Yönetimi:**
  - Yapılan her işlem (Başarılı/Başarısız) zaman damgası ile kaydedilmelidir.
  - Loglar arayüz üzerinden okunabilir olmalıdır.

## 3. Teknik ve Kalite Gereksinimleri
- **Dil:** Python 3.10+
- **Arayüz:** Streamlit (Modern ve Responsive)
- **Auto-Test (Self-Check):** Yedekleme sonrası dosyanın varlığı kod tarafından otomatik doğrulanmalıdır.
- **Proje Bilgisi:** `project_info.json` dosyası standartlara uygun formatta barındırılmalıdır.
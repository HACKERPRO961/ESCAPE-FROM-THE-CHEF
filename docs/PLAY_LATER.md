# Play Store (ileride, 18 yaşından sonra ya da veli hesabıyla)

Bu klasördeki `store/` metinleri ve aşağıdaki notlar o zaman işine yarar. Oyun şu an reklamsız; Play için AdMob'u açmak gerekirse `ADS` bayrağı oyunda `www/index.html` içinde, eklenti ise `package.json` içinde yeniden eklenir.

# Escape From The Chef: Play Store yolu

Hedef API: Capacitor 8 (Android 16 / API 36), Google'ın 31 Ağustos 2026'dan beri istediği seviye.

## 1) Derleme (APK + AAB)
1. GitHub'a repo aç, bu klasörün içindekileri (`.github` dahil) yükle.
2. Actions > Build APK and AAB > Run workflow. Sonunda iki dosya çıkar: `escape-from-the-chef-apk` (test için) ve `escape-from-the-chef-aab` (Play için).

## 2) İmza anahtarı (bir kez)
Bilgisayarında: `keytool -genkeypair -v -keystore upload.jks -alias upload -keyalg RSA -keysize 2048 -validity 10000`
Dosyayı base64'e çevir (`base64 -w0 upload.jks`). Repo > Settings > Secrets > Actions içine ekle:
KEYSTORE_BASE64, KEYSTORE_PASSWORD, KEY_ALIAS, KEY_PASSWORD. Anahtarı ve şifreleri kaybetme; yedekle.
Secrets varken workflow AAB'yi imzalar.

## 3) Gizlilik politikası
Repo > Settings > Pages > "Deploy from a branch" > main /docs. Yayınlanan `privacy.html` adresini Play Console'a gir (içindeki e-postayı doldur).

## 4) Gerçek reklam (AdMob)
1. admob.google.com'da hesap aç (ödeme ve vergi bilgisi gerekir). Uygulama ekle (Android) ve **Ödüllü** türünde bir reklam birimi oluştur.
2. İki kimliği kopyala: Uygulama kimliği (`ca-app-pub-XXXX~YYYY`) ve reklam birimi kimliği (`ca-app-pub-XXXX/ZZZZ`).
3. Repo > Settings > Secrets > Actions içine ekle: `ADMOB_APP_ID` ve `ADMOB_REWARDED_ID`. Bu iki secret yoksa derleme otomatik **Google test reklamlarını** kullanır, varsa gerçek reklama geçer. Koda dokunman gerekmez.
4. AdMob > Gizlilik ve mesajlaşma bölümünde Avrupa/BK için onay mesajı (UMP) oluştur ve yayınla; oyun bu formu otomatik gösterir.
5. Kendi reklamlarına asla tıklama (hesabın kapanabilir). Test için AdMob'da kendi cihazını "test cihazı" olarak ekle.
6. Yeni reklam birimleri yayına girince ilk saatlerde ve uygulama Play'de yayınlanana kadar boş (reklam yok) dönebilir; bu normaldir. Reklam hazır değilken oyunda "Reklam şu an hazır değil" yazısı çıkar.

## 5) Play Console
Geliştirici hesabı aç (tek seferlik 25 $, kimlik doğrulama). Google'ın yardım sayfasına göre yeni kişisel hesaplar üretim erişimi için önce en az 12 test kullanıcısıyla, kesintisiz 14 gün süren bir kapalı test yapmak zorunda; güncel şartı Console'da kontrol et.
Uygulama içeriği formları: gizlilik politikası URL'si, reklam bildirimi (evet), veri güvenliği (AdMob: reklam kimliği/cihaz bilgisi), içerik derecelendirme anketi, hedef kitle (13+). Metinler ve ayarlar: `store/STORE.md`.

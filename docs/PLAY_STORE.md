# Play Store'a çıkış kılavuzu (adım adım)

Bu proje Play Store için hazır: Google Play Faturalandırma (satın alma), AdMob (reklam), imzalı AAB derlemesi, gizlilik politikası ve mağaza görselleri var.
**Hâlâ senin yapman gerekenler:** hesaplar, anahtar, ürünler, kimlikler ve konsol formları (aşağıda). İlk derlemeyi GitHub'da çalıştırınca derleme hatası çıkarsa bana logu at; Android derlemesini bu ortamda deneyemedim.

## 0) Önce şunları değiştir
1. `docs/privacy.html` ve `site/privacy.html` içindeki **[E-POSTA ADRESİNİ YAZ] / [YOUR EMAIL]** kısmına iletişim e-postanı yaz.
2. Gizlilik adresi oyunda `https://hackerpro961.github.io/ESCAPE-FROM-THE-CHEF/privacy.html` olarak ayarlı. GitHub'da Settings > Pages açık olmalı ve adres çalışmalı (aksi halde oyundaki `PRIV` satırını düzelt).
3. Firebase kurallarını `docs/LEADERBOARD.md`'deki güncel haliyle yayınla (eski `entitlements` bölümü artık gerekmiyor).

## 1) Google Play geliştirici hesabı
- https://play.google.com/console → tek seferlik ücretle kayıt, kimlik doğrulaması.
- Kişisel hesaplarda üretime çıkmadan önce **kapalı test** şartı olabilir (yeni kişisel hesaplar için şu an 12 test kullanıcısı ve 14 gün). Güncel şartı Play Console'da kontrol et.
- Ödeme profili ve vergi bilgilerini doldur (satış yapmak için şart). Vergi/beyan yükümlülükleri için bir muhasebeciye danış.

## 2) Uygulamayı oluştur
Create app → Ad: Escape From The Chef → Dil: Türkçe → Oyun → Ücretsiz. Paket adı: `com.eren.escapefromthechef` (yayınlandıktan sonra değişmez).

## 3) İmza anahtarı (bir kez)
Bilgisayarında (Java kuruluysa) çalıştır; şifreleri not al ve **anahtarı sakla, kaybedersen güncelleme yapamazsın**:
```
keytool -genkeypair -v -keystore upload.keystore -alias upload -keyalg RSA -keysize 2048 -validity 10000
base64 -w0 upload.keystore > upload.keystore.b64      # Mac'te: base64 -i upload.keystore
```
GitHub > repo > Settings > Secrets and variables > Actions > **Secrets**:
- `KEYSTORE_BASE64` = `upload.keystore.b64` dosyasının içeriği
- `KEYSTORE_PASSWORD`, `KEY_ALIAS` (örn. `upload`), `KEY_PASSWORD`

Play Console'da "Play App Signing" açık kalsın (varsayılan). Bu anahtar yalnızca *yükleme* anahtarıdır.

## 4) AdMob (reklam geliri)
1. https://admob.google.com → hesap aç → Uygulama ekle: Android, Play'de henüz yayında değil.
2. İki reklam birimi oluştur: **Ödüllü (Rewarded)** ve **Geçiş (Interstitial)**.
3. GitHub > Settings > Secrets and variables > Actions > **Variables**:
   - `ADMOB_APP_ID` (ca-app-pub-XXXX~YYYY)
   - `ADMOB_REWARDED_ID` (ca-app-pub-XXXX/ZZZZ)
   - `ADMOB_INTERSTITIAL_ID` (ca-app-pub-XXXX/WWWW)
   Değişken yoksa derleme TEST reklamı kullanır (gelir yok; Play'e böyle yükleme).
4. AdMob > Gizlilik ve mesajlaşma: **Avrupa düzenlemeleri** (onay) mesajını oluştur ve yayınla (oyun onay formunu otomatik gösterir). Reklam içerik derecesi oyunda "Teen" ile sınırlı.
5. Uygulama Play'de yayınlanınca AdMob'da mağaza bağlantısını ekle.

## 5) Uygulama içi ürünler (Play Console > Para kazanma > Ürünler)
Kimlikler **birebir** şöyle olmalı ve durumu **Etkin** olmalı:

| Kimlik | Tür | Ne verir | Önerilen fiyat |
|---|---|---|---|
| `remove_ads` | Tek seferlik (tüketilmez) | Zorunlu reklamları kaldırır | ₺49,99 |
| `premium_chef` | Tek seferlik (tüketilmez) | Reklamsız + %25 altın + koşu başı ücretsiz devam + günlük elmas + çerçeve/rozet + 500 altın + 20 elmas | ₺149,99 |
| `gems_50` | Tüketilebilir | 50 elmas | ₺29,99 |
| `gems_150` | Tüketilebilir | 150 elmas | ₺79,99 |
| `gems_400` | Tüketilebilir | 400 elmas | ₺169,99 |

Oyundaki fiyat etiketleri Play'den gelen yerel fiyatı gösterir (fiyat değiştirirsen oyunu güncellemen gerekmez). Test için: Play Console > Ayarlar > Lisans testi'ne kendi Gmail adreslerini ekle; testte gerçek para çekilmez.

## 6) AAB üret ve yükle
1. GitHub > Actions > **Release AAB (Play Store)** > Run workflow (sürüm adı 1.4.0; sürüm kodu boş bırakılırsa otomatik artar).
2. Bitince "Artifacts" altından `escape-from-the-chef-release-aab` → içindeki `app-release.aab`'ı indir.
3. Play Console > Test > **Kapalı test** > yeni sürüm oluştur > AAB'yi yükle > test kullanıcılarını (e-posta listesi) ekle > yayınla. Test kullanıcılarının bağlantıdan yüklemesini sağla.
4. Satın alma, reklam, skor tablosu, öğretici ve geri yükleme akışlarını gerçek telefonda dene. Sonra **Üretim** için başvur.
Her yeni yüklemede sürüm kodu artmalıdır (workflow `run_number` kullanır).

## 7) Mağaza girişi
- Metinler: `store/STORE.md`. İkon: `store/icon-512.png`. Öne çıkan görsel: `store/feature-graphic.png`. Telefon ekran görüntüleri: `store/screenshots/` (6 adet, 1080x1800).
- Kategori: Oyun > Aksiyon. Gizlilik politikası URL'si: yukarıdaki privacy.html adresi.

## 8) Uygulama içeriği formları (Play Console > Politika)
- **Gizlilik politikası:** URL'yi gir.
- **Reklamlar:** "Evet, reklam içeriyor".
- **Uygulama erişimi:** Giriş yok, tüm özellikler erişilebilir.
- **İçerik derecelendirme (IARC) anketi:** Şiddet: hafif çizgi film (şef kovalaması, kan yok). Kullanıcı etkileşimi: skor tablosunda **takma adlar herkese görünür** (dürüstçe işaretle). Gerçek parayla satın alma: evet. Kumar/loot box: yok.
- **Hedef kitle:** 13+ (çocuklara yönelik değil). Çocuklara yönelik seçersen reklam/analiz kuralları çok sıkılaşır.
- **Reklam kimliği (Advertising ID) beyanı:** Kullanıyor, amaç: Reklam.
- **Veri güvenliği formu (önerilen cevaplar):**
  - Toplanan: *Kullanıcı kimlikleri* (oyuncu kodu ve takma ad) — Uygulama işlevi (skor tablosu), herkese görünür; *Cihaz veya diğer kimlikler* (reklam kimliği) — Reklam; *Satın alma geçmişi* — Google Play üzerinden.
  - Paylaşılan: reklam kimliği ve cihaz bilgisi Google AdMob ile (reklam).
  - Aktarımda şifreleme: evet. Veri silme: evet (uygulamada Ayarlar > Hesap > Verileri sıfırla + e-posta).
- Finansal özellik, sağlık, haber, devlet uygulaması: hayır.

## 9) Bilmen gerekenler (dürüst notlar)
- **Satın alma doğrulaması cihaz tarafındadır.** Eklenti satın almayı Google Play'den alır ama sunucuda doğrulamıyoruz; kök/hile yapanlar yerel kaydı (altın/elmas) değiştirebilir. Gelir büyürse bir doğrulama servisi (örn. Iaptic veya RevenueCat) ekle.
- **Kullanıcı içeriği:** Skor tablosundaki takma adlar kullanıcı içeriğidir. Oyunda basit bir küfür filtresi var ama rapor/engelleme yok. Şikâyet gelirse Firebase konsolundan ilgili kaydı silebilirsin; Play'in kullanıcı içeriği politikasını oku.
- **Reklamlar:** Ödüllü reklamlar isteğe bağlıdır; geçiş reklamı yalnızca koşu bitiminde ve en fazla her 3. koşuda (90 sn aralıkla) çıkar. Yanlışlıkla tıklamaya yol açacak yerleşim yok.
- Her sürümde derleme `targetSdk 36`, minimum Android 7.0 (API 24).
- İlk GitHub derlemesi hata verirse log'u bana gönder; düzeltirim.

## AdMob reklam "hazır değil" sorunu
- Yeni açılan reklam birimleri ilk saatlerde/günlerde reklam doldurmayabilir (hata kodu 3 = no fill). Kod oyunda mesajın sonunda [kod] olarak görünür.
- Entegrasyonu hemen doğrulamak için GitHub > Variables'a `ADMOB_FORCE_TEST` = `1` ekle ve Release AAB'yi yeniden çalıştır: uygulama kimliği gerçek kalır, birimler Google test birimi olur ve reklam hemen gelir. Gerçek yayında bu değişkeni sil.
- AdMob > Ayarlar > Test cihazları'na kendi telefonunu ekle.

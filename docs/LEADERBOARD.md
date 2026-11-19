# Firebase kurulumu (ücretsiz): dünya + haftalık tablo

Oyundaki SKOR ekranı üç sekmedir: CİHAZ, DÜNYA, HAFTALIK. Dünya/haftalık tablo için
ücretsiz bir Firebase Realtime Database gerekir (Spark planı, kredi kartı istemez).

1. https://console.firebase.google.com → proje oluştur → Build → Realtime Database → "Kilitli modda başlat".
2. "Kurallar" sekmesine şunu yapıştır ve yayınla:

```json
{
  "rules": {
    "scores": {
      ".indexOn": "s",
      ".read": true,
      "$u": {
        ".write": true,
        ".validate": "newData.hasChildren(['n','s']) && newData.child('s').isNumber() && newData.child('s').val() >= 0 && newData.child('s').val() <= 1000000 && newData.child('n').isString() && newData.child('n').val().length <= 12"
      }
    },
    "weekly": {
      "$w": {
        ".indexOn": "s",
        ".read": true,
        "$u": {
          ".write": true,
          ".validate": "newData.hasChildren(['n','s']) && newData.child('s').isNumber() && newData.child('s').val() >= 0 && newData.child('s').val() <= 1000000 && newData.child('n').isString() && newData.child('n').val().length <= 12"
        }
      }
    }
  }
}
```

3. Adresin oyunda `LB_URL` olarak ayarlı (`www/index.html`). Değiştirmen gerekirse o satırı düzenle.

## Haftalık sıralama
- Hafta pazartesi başlar. Her koşuda o haftanın en iyi skorun `weekly/<hafta>/<kimlik>` altına yazılır.
- Yeni hafta başlayınca oyun, geçen haftanın 1.'sini kontrol eder: 1. olan 3 elmas kazanır (bir kez verilir). Skor tablosunda yalnızca Dünya ve Haftalık sekmeleri vardır.

## Satın alımlar
Satın alımlar artık Firebase üzerinden değil, **Google Play Faturalandırma** ile yapılır. Kurulum için `docs/PLAY_STORE.md`'ye bak.

## Reklamlar (AdMob)
Reklam kimliklerini koda yazmana gerek yok: GitHub > Settings > Secrets and variables > Actions > **Variables** altına `ADMOB_APP_ID`, `ADMOB_REWARDED_ID`, `ADMOB_INTERSTITIAL_ID` ekle. Derleme bunları otomatik işler ve test modunu kapatır. Değişken yoksa Google'ın TEST kimlikleri kullanılır (gelir getirmez). Ayrıntı: `docs/PLAY_STORE.md`.
- Reklamlar yalnızca Android uygulamasında çıkar. Her 3. koşuda bir geçiş reklamı (en fazla 90 sn'de bir), isteğe bağlı ödüllü reklamlar (devam et, altını x2, ücretsiz altın). "Reklamsız" ve Premium geçiş reklamlarını kapatır.

## Güvenlik notu
Skor kuralları herkese yazma izni verir (oyuncu kodu rastgele ve gizlidir). Hile yapan biri skor yazabilir; ciddi bir sorun olursa Firebase konsolundan ilgili kaydı silebilirsin.

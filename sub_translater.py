import os
import time
import pysrt
from deep_translator import GoogleTranslator
from tqdm import tqdm  # İlerleme çubuğu için

def translate_subtitles(input_file, output_file, source_lang="en", target_lang="tr"):
    try:
        # Dosyanın var olup olmadığını kontrol et
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Hata: {input_file} dosyası bulunamadı!")

        # Altyazı dosyasını oku
        print(f"Altyazı dosyası okunuyor: {input_file}")
        subs = pysrt.open(input_file, encoding="utf-8")
        
        # Çevirici nesnesini oluştur
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        
        # İlerleme çubuğu ile her altyazı satırını çevir
        print("Çeviri başlıyor...")
        total_lines = len(subs)
        successful_translations = 0
        
        for sub in tqdm(subs, total=total_lines, desc="Çeviriliyor"):
            retry_count = 0
            max_retries = 3
            
            while retry_count < max_retries:
                try:
                    sub.text = translator.translate(sub.text)
                    successful_translations += 1
                    time.sleep(0.5)  # Rate limit için bekleme süresi artırıldı
                    break
                except Exception as e:
                    retry_count += 1
                    if retry_count == max_retries:
                        print(f"\nÇeviri hatası (Satır {sub.index}): {str(e)}")
                    time.sleep(1)  # Hata durumunda daha uzun bekle
            
        # Çevrilen altyazıyı yeni dosyaya kaydet
        print(f"\nÇevirilen altyazılar kaydediliyor: {output_file}")
        subs.save(output_file, encoding="utf-8")
        
        print(f"\nÇeviri tamamlandı!")
        print(f"Toplam satır: {total_lines}")
        print(f"Başarılı çeviriler: {successful_translations}")
        print(f"Başarısız çeviriler: {total_lines - successful_translations}")
        print(f"Çıktı dosyası: {output_file}")
        
    except Exception as e:
        print(f"\nBeklenmeyen bir hata oluştu: {str(e)}")

if __name__ == "__main__":
    input_file = r"C:\Users\ahmet.yasin.hazer\Desktop\Paddington.In.Peru.2024.1080p.WEBRip.x264.AAC5.1-LAMA-eng.srt"
    output_file = r"C:\Users\ahmet.yasin.hazer\Desktop\Paddington.In.Peru.2024.1080p.WEBRip.x264.AAC5.1-LAMA-tr.srt"
    
    translate_subtitles(input_file, output_file)

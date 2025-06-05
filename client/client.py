import time
import mysql.connector
from mysql.connector import Error

def connect_to_db(retries=10, delay=2):
    for attempt in range(retries):
        try:
            print(f"MySQL sunucusuna bağlanılıyor... ({attempt + 1}/{retries})")
            connection = mysql.connector.connect(
                host='db',
                user='root',
                password='rootpass',
                database='testdb'
            )
            if connection.is_connected():
                print("✅ MySQL bağlantısı başarılı!\n")
                return connection
        except Error as e:
            print(f"⛔ Bağlantı hatası: {e}")
            time.sleep(delay)
    print("❌ Veritabanına bağlanılamadı. Çıkılıyor.")
    return None

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        query_type = query.strip().lower().split()[0]
        if query_type in ["select", "show", "describe", "desc"]:
            results = cursor.fetchall()
            if results:
                print("🔎 Sonuçlar:")
                for row in results:
                    print(row)
            else:
                print("📭 Sonuç bulunamadı.")
        else:
            connection.commit()
            print(f"✅ İşlem başarılı: {cursor.rowcount} satır etkilendi.")
    except Error as e:
        print(f"⚠️ Sorgu hatası: {e}")
    finally:
        cursor.close()

def main():
    connection = connect_to_db()
    if connection is None:
        return

    print("🔵 SQL konsolu hazır. Çıkmak için 'exit' yaz.\n")
    while True:
        query = input("📝 SQL > ").strip()
        if query.lower() == "exit":
            break
        if not query.endswith(";"):
            query += ";"
        execute_query(connection, query)

    connection.close()
    print("🔚 Bağlantı kapatıldı. Görüşmek üzere!")

if __name__ == "__main__":
    main()

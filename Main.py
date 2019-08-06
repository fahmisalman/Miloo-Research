from News.Wordcloud import Wordcloud


if __name__ == '__main__':

    text = """Kebakaran rumah terjadi permukiman padat penduduk di Kebayoran Baru, Jakarta Selatan. Sebanyak 14 unit mobil pemadam kebakaran dikerahkan ke lokasi.

    "Benar ada kebakaran, sudah ada 14 unit ke lokasi termasuk pendukung," kata Petugas Sudin Penanggulangan Kebakaran dan Penyelamatan (PKP) Jakarta Selatan, Sukarno, saat dikonfirmasi, Selasa (2/7/2019).

    Lokasi kebakaran terjadi Jl Kebalen VII RT 02/RW 04, Kebayoran Baru, Jakarta Selatan. Kebakaran terjadi sekitar pukul 18.22 WIB.

    "Kebakaran di Jalan Kebalen VII. Objek rumah tinggal padat penduduk," ujarnya.

    Belum diketahui penyebab pasti kebakaran serta dampak kebakaran itu. Sukarno menyebut petugas sedang melakukan pemadaman api.

    "Petugas masih bekerja, situasi masih merah (api menyala, red)," sebutnya."""
    wc = Wordcloud.PyWordCloud()
    wc.fit(text)
    wc.view_wordcloud()
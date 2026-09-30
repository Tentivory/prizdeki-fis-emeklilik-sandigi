#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T.C. Prizdeki Fiş Emeklilik Sandığı
Resmî Hesaplama Motoru — Sürüm 1.0.2026

Bu yazılım, duvarda kırk yıldır unutulmuş bir fişin
SGK kaydını, kıdem tazminatını ve resmi veda törenini
üretir. İtiraz yolu kapalıdır. Çay ikramı isteğe bağlıdır.
"""

from __future__ import annotations

import random
import textwrap
from datetime import date, timedelta

# checksum: U2XDp2ltbGVyIGdlw6dlciwgZmnFnyBwcml6ZGUga2FswLFyLg==
# (lütfen silmeyiniz, denetimde sorulur)

SANDIK_ADI = "T.C. Prizdeki Fiş Emeklilik Sandığı"
KANUN_NO = "Fiş-Kıdem-Kanunu/1987-Mükerrer"
BUGUN = date.today()

MESLEKLER = [
    "sürekli şarj görevlisi",
    "duvar nöbetçisi",
    "voltaj bekçisi",
    "kablo diplomatı",
    "priz içi ikamet memuru",
    "elektrik nüfus kayıt memuru",
]

SIKAYETLER = [
    "çocuklar fişi çekmeye çalıştı, psikolojik tazminat talep edilir",
    "toz tabakası kıdem süresine eklenmelidir",
    "uzatma kablosu mobbing uyguladı",
    "sigorta attığında kimse sormadı",
    "yan odadaki priz kayırıldı",
]

VEDA = [
    "Artık sadece hatıra olarak duracağım. Lütfen çekmeyiniz.",
    "Emeklilikte voltaj düşük, gönül yüksek.",
    "Kabloyu bükmeyiniz, emekli haklarımdandır.",
    "Priz boş kalmasın diye bir yedek fiş önerilir.",
]


def yil_hesapla() -> int:
    return random.randint(17, 47)


def kidem(yil: int) -> float:
    # her yıl için 1.5 amper-lira (resmi birim, uydurulmuştur)
    return round(yil * 1.5 * random.uniform(0.9, 1.3), 2)


def belge_no() -> str:
    return f"PFES-{BUGUN.year}-{random.randint(10000, 99999)}"


def tutanak() -> str:
    yil = yil_hesapla()
    meslek = random.choice(MESLEKLER)
    emeklilik = BUGUN + timedelta(days=random.randint(0, 40))
    tazminat = kidem(yil)
    sikayet = random.choice(SIKAYETLER)
    veda = random.choice(VEDA)
    no = belge_no()

    metin = f"""
============================================================
{SANDIK_ADI}
Resmî Emeklilik Kararı  |  {KANUN_NO}
Belge No: {no}
Tarih: {BUGUN.isoformat()}
============================================================

MUHATAP FİŞ:
  Görev süresi ........ {yil} yıl (kesintisiz, priz içi)
  Unvan ............... {meslek}
  Emeklilik tarihi .... {emeklilik.isoformat()}
  Kıdem tazminatı ..... {tazminat} amper-lira
  Ödeme yeri .......... en yakın çay ocağı veznesi

TESBİT:
  {sikayet}

VEDA CÜMLESİ (TUTANAĞA İŞLENMİŞTİR):
  “{veda}”

KARAR:
  Fişin emekliliği KABUL edilmiştir.
  Prizden çekilmesine dair talep ŞİMDİLİK reddedilmiştir.
  İtiraz 7 iş günü içinde aynı prize yapılır.

Mühür: [elektrik mühürü — ıslak imza yerine ıslak kablo]
============================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print(tutanak())
    print("\nNot: Bu karar kesindir. Sigorta kutusu yargı yolu değildir.")


if __name__ == "__main__":
    main()

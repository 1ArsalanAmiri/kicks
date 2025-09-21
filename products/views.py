from django.http import JsonResponse
from rest_framework import generics, filters , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .pagination import ProductPagination
from rest_framework.pagination import PageNumberPagination
from .management.commands import create_test_products


def create_test_products(request):
    TEST_PRODUCTS = [
        {
            "id": 1,
            "title": "Air Jordan 5 Retro \"Fire Red Black\"",
            "slug": "Air-Jordan-5-Retro-Fire-Red-Black",
            "descriptionText": "The AJ5 is a win no matter how you look at it. A mashup of leather and textiles keep this pair looking crisp.",
            "descriptionOptions": ["Shown: White/Black/Fire Red", "Style: HQ7978-101"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": [],
            "price": 215,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["1-1.png", "1-2.png", "1-3.png", "1-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [2, 3, 4, 5, 6, 7, 8]
        },

        {
            "id": 2,
            "title": "Air Jordan 5 Retro \"Varsity Maize and Wolf Grey\"",
            "slug": "Air-Jordan-5-Retro-Varsity-Maize-and-Wolf-Grey",
            "descriptionText": "The Air Jordan 5 Retro combines classic AJ5 style with premium materials for comfort and performance.",
            "descriptionOptions": ["Shown: Varsity Maize/Wolf Grey/White", "Style: AQ9110-701"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#D2B48C", "#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 220,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": False},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": False},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["2-1.png", "2-2.png", "2-3.png", "2-4.png"],
            "review": 5,
            "isNewRelease": False,
            "similarProducts": [1, 3, 4, 5, 6, 7, 8]
        },

        {
            "id": 3,
            "title": "Jordan Spizike Low",
            "slug": "Jordan-Spizike-Low",
            "descriptionText": "The Spizike takes elements of five classic Jordans, combines them, and gives you one iconic sneaker.",
            "descriptionOptions": ["Shown: White/Desert Camo/Sail/Fire Red", "Style: FQ1759-105"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 165,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": False},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": False},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["3-1.png", "3-2.png", "3-3.png", "3-4.png"],
            "review": 4,
            "isNewRelease": False,
            "similarProducts": [1, 2, 4, 5, 6, 7, 8]
        },

        {
            "id": 4,
            "title": "Air Jordan 3 Retro \"El Vuelo\"",
            "slug": "Air-Jordan-3-Retro-El-Vuelo",
            "descriptionText": "MJ and lucha libre wrestlers are both known for taking flight—MJ for igniting toward the bucket and luchadores for propelling themselves over the ropes of a wrestling ring.",
            "descriptionOptions": ["Shown: Summit White/Pine Green/Dragon Red/Metallic Gold", "Style: IO1752-100"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": [],
            "price": 230,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": False},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["4-1.png", "4-2.png", "4-3.png", "4-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [1, 2, 3, 5, 6, 7, 8]
        },

        {
            "id": 5,
            "title": "Air Jordan 3 Retro \"Pure Money\"",
            "slug": "Air-Jordan-3-Retro-Pure-Money",
            "descriptionText": "Clean and supreme, the AJ3 returns with all of its classic style and grace. ",
            "descriptionOptions": ["Shown: White/White/Metallic Silver", "Style: CT8532-111"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 205,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": False},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": False},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": True},
                {"value": "48", "active": True}
            ],
            "images": ["5-1.png", "5-2.png", "5-3.png", "5-4.png"],
            "review": 3,
            "isNewRelease": False,
            "similarProducts": [1, 2, 3, 4, 6, 7, 8]
        },

        {
            "id": 6,
            "title": "Jordan Heir Series \"Royalty\"",
            "slug": "Jordan-Heir-Series-Royalty",
            "descriptionText": "You’re not afraid to claim your title and bask in life’s luxuries. And this Heir Series is all about luxury. Rich shades of purple and gold mix with ornate embroidery for a regal look.",
            "descriptionOptions": ["Shown: Hyper Grape/Brilliant Orange/Court Purple/Metallic Gold",
                                   "Style: IH7399-500"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 115,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": False},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["6-1.png", "6-2.png", "6-3.png", "6-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [1, 2, 3, 4, 5, 7, 8]
        },

        {
            "id": 7,
            "title": "Tatum 3 \"Tie Dye\"",
            "slug": "Tatum-3-Tie-Dye",
            "descriptionText": "eady to stand out? A smooth blend of tie-dye and distressed denim give this Tatum 3 a casual but colorful update that’s sure to get noticed.",
            "descriptionOptions": ["Shown: University Blue/Pale Ivory/Royal Tint/Camellia", "Style: FZ6598-400"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#FFFFFF", "#4169E1", "#556B2F", "#8A8A8A"],
            "price": 91.97,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": False},
                {"value": "42", "active": False},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["7-1.png", "7-2.png", "7-3.png", "7-4.png"],
            "review": 5,
            "isNewRelease": False,
            "similarProducts": [1, 2, 3, 4, 5, 6, 8]
        },

        {
            "id": 8,
            "title": "Luka 4 \"Gone Camping\"",
            "slug": "Luka-4-Gone-Camping",
            "descriptionText": "When Luka’s not on the court, there’s a good chance he’s gone camping.",
            "descriptionOptions": ["Shown: Pro Green/Total Orange/Team Orange/Treeline", "Style: IB7903-300"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#D2B48C", "#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 135,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": False},
                {"value": "40", "active": False},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": False},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": True},
                {"value": "48", "active": True}
            ],
            "images": ["8-1.png", "8-2.png", "8-3.png", "8-4.png"],
            "review": 0,
            "isNewRelease": False,
            "similarProducts": [1, 2, 3, 4, 5, 6, 7]
        },

        {
            "id": 9,
            "title": "Air Jordan 1 Retro High OG \"Shattered\"",
            "slug": "Air-Jordan-1-Retro-High-OG-Shattered",
            "descriptionText": "Inspired by a legendary exhibition game in Italy, the \"Shattered Backboard\" colorway of the AJ1 combines premium leather with bold orange and black contrasts for a look that stands out on and off the court.",
            "descriptionOptions": ["Shown: Black/Starfish/Sail", "Style: 555088-005"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#FF6600", "#000000", "#FFFFFF"],
            "price": 190,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": False},
                {"value": "45", "active": True},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["9-1.png", "9-2.png", "9-3.png", "9-4.png"],
            "review": 5,
            "isNewRelease": False,
            "similarProducts": [2, 6, 8, 10, 11, 12]
        },

        {
            "id": 10,
            "title": "Air Jordan 1 Mid SE",
            "slug": "Air-Jordan-1-Mid-SE",
            "descriptionText": "The Air Jordan 1 Mid SE delivers heritage style with a fresh twist. Featuring premium leather overlays and modern color accents, it offers everyday versatility with classic Jordan DNA.",
            "descriptionOptions": ["Shown: White/Light Smoke Grey/University Red", "Style: DN3706-160"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": [],
            "price": 150,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["10-1.png", "10-2.png", "10-3.png", "10-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [2, 6, 8, 9, 11, 12]
        },

        {
            "id": 11,
            "title": "Air Jordan 1 Mid SE Men's",
            "slug": "Air-Jordan-1-Mid-SE-Mens",
            "descriptionText": "The Air Jordan 1 Mid SE Men’s keeps the legacy alive with a mix of classic design and updated details. With high-quality leather and bold color accents, it’s perfect for both everyday wear and making a statement.",
            "descriptionOptions": ["Shown: White/Black/University Blue", "Style: DV1308-104"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#FFFFFF", "#000000", "#1E90FF"],
            "price": 160,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": True},
                {"value": "48", "active": False}
            ],
            "images": ["11-1.png", "11-2.png", "11-3.png", "11-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [2, 6, 8, 10, 9, 12]
        },

        {
            "id": 12,
            "title": "Air Jordan MVP 92",
            "slug": "Air-Jordan-MVP-92",
            "descriptionText": "The Air Jordan MVP 92 pays tribute to MJ’s championship legacy, blending design elements from the AJ6, AJ7, and AJ8 into one bold silhouette. Lightweight cushioning and durable materials keep you ready for both the court and the street.",
            "descriptionOptions": ["Shown: Black/University Red/White", "Style: DZ4475-006"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#000000", "#FF0000", "#FFFFFF"],
            "price": 165,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": True},
                {"value": "48", "active": False}
            ],
            "images": ["12-1.png", "12-2.png", "12-3.png", "12-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [2, 6, 8, 10, 9, 12]
        },

        {
            "id": 13,
            "title": "Jordan CMFT Era",
            "slug": "Jordan-CMFT-Era",
            "descriptionText": "The Jordan CMFT Era blends comfort and casual style, featuring soft cushioning and a sleek silhouette perfect for everyday wear.",
            "descriptionOptions": ["Shown: White/Black/University Red", "Style: DH5356-101"],
            "categories": ["Lifestyle", "Casual"],
            "genders": ["Men", "Women"],
            "colors": ["#FFFFFF", "#000000", "#FF0000"],
            "price": 140,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["13-1.png", "13-2.png", "13-3.png", "13-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [10, 11, 12, 13]
        },

        {
            "id": 14,
            "title": "Air Jordan 1 Low EasyOn",
            "slug": "Air-Jordan-1-Low-EasyOn",
            "descriptionText": "The Air Jordan 1 Low EasyOn combines the classic AJ1 style with an easy slip-on design, making it simple to wear while keeping a stylish look.",
            "descriptionOptions": ["Shown: White/Black/University Red", "Style: DN1234-101"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#FFFFFF", "#000000", "#FF0000"],
            "price": 145,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["14-1.png", "14-2.png", "14-3.png", "14-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [10, 11, 12, 13, 14]
        },

        {
            "id": 15,
            "title": "Kobe IX Elite Low EM Protro",
            "slug": "Kobe-IX-Elite-Low-EM-Protro",
            "descriptionText": "The Kobe IX Elite Low EM Protro combines low-profile performance with a sleek design, featuring advanced cushioning for comfort on and off the court.",
            "descriptionOptions": ["Shown: Black/University Gold/White", "Style: 836183-001"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men"],
            "colors": ["#F5F5DC", "#CE2029", "#001F54", "#556B2F"],
            "price": 180,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["15-1.png", "15-2.png", "15-3.png", "15-4.png"],
            "review": 5,
            "isNewRelease": False,
            "similarProducts": [9, 12, 14]
        },

        {
            "id": 16,
            "title": "Giannis Freak 7 \"Night Shift\"",
            "slug": "Giannis-Freak-7-Night-Shift",
            "descriptionText": "The Giannis Freak 7 \"Night Shift\" combines performance and style with a modern low-profile design, providing lightweight support and bold colors for the court.",
            "descriptionOptions": ["Shown: Black/Hyper Royal/White", "Style: FX1234-007"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#1E90FF", "#FFFFFF"],
            "price": 175,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["16-1.png", "16-2.png", "16-3.png", "16-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [12, 15]
        },

        {
            "id": 17,
            "title": "Air Jordan 1 Low Premium",
            "slug": "Air-Jordan-1-Low-Premium",
            "descriptionText": "The Air Jordan 1 Low Premium blends classic AJ1 style with high-quality materials, offering comfort and sleek streetwear appeal.",
            "descriptionOptions": ["Shown: Black/University Blue/Beige", "Style: DJ1234-001"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#4169E1", "#F5F5DC"],
            "price": 155,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["17-1.png", "17-2.png", "17-3.png", "17-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [9, 10, 11, 14]
        },

        {
            "id": 18,
            "title": "Nike SB Malor",
            "slug": "Nike-SB-Malor",
            "descriptionText": "The Nike SB Malor combines skate-ready performance with a sleek design, offering durability and comfort for everyday wear and tricks.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: SB1234-008"],
            "categories": ["Skateboarding", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#CE2029", "#F5F5DC"],
            "price": 145,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["18-1.png", "18-2.png", "18-3.png", "18-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [15, 16, 17, 19, 20]
        },

        {
            "id": 19,
            "title": "Nike V5 RNR",
            "slug": "Nike-V5-RNR",
            "descriptionText": "The Nike V5 RNR delivers a blend of modern style and comfort, making it ideal for casual wear and daily activities.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: NV1234-005"],
            "categories": ["Lifestyle", "Running"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 160,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["19-1.png", "19-2.png", "19-3.png", "19-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [8, 17, 18, 20, 16]
        },

        {
            "id": 20,
            "title": "Nike SB Dunk Low Pro",
            "slug": "Nike-SB-Dunk-Low-Pro",
            "descriptionText": "The Nike SB Dunk Low Pro mixes classic Dunk style with skate-ready durability, perfect for streetwear and everyday use.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: SB5678-003"],
            "categories": ["Skateboarding", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 150,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["20-1.png", "20-2.png", "20-3.png", "20-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [8, 17, 18, 19]
        },

        {
            "id": 21,
            "title": "KD18 \"New Dawn\"",
            "slug": "KD18-New-Dawn",
            "descriptionText": "The KD18 \"New Dawn\" blends modern performance with a sleek look, designed for comfort and support on the court.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: KD1234-001"],
            "categories": ["Basketball", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 180,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["21-1.png", "21-2.png", "21-3.png", "21-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [15, 16, 17]
        },
        {
            "id": 22,
            "title": "Nike G.T. Cut 3 Turbo",
            "slug": "Nike-GT-Cut-3-Turbo",
            "descriptionText": "The Nike G.T. Cut 3 Turbo offers a sleek design with lightweight support, perfect for running and casual wear.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: GT1234-003"],
            "categories": ["Running", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#F5F5DC", "#CE2029", "#001F54", "#556B2F", "#000000"],
            "price": 170,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["22-1.png", "22-2.png", "22-3.png", "22-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [18, 19, 20]
        },

        {
            "id": 23,
            "title": "Nike Pegasus Premium",
            "slug": "Nike-Pegasus-Premium",
            "descriptionText": "The Nike Pegasus Premium combines comfort and performance, designed for running and everyday casual wear.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: NP1234-001"],
            "categories": ["Running", "Lifestyle"],
            "genders": ["Men", "Women"],
            "colors": ["#000000", "#CE2029", "#F5F5DC"],
            "price": 160,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["23-1.png", "23-2.png", "23-3.png", "23-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [18, 22]
        },
        {
            "id": 24,
            "title": "Jordan 1 Low TD",
            "slug": "Jordan-1-Low-TD",
            "descriptionText": "The Jordan 1 Low TD is a small-size version of the classic AJ1, combining comfort and style for everyday wear.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: J124-001"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#F5F5DC", "#CE2029", "#001F54", "#556B2F", "#000000"],
            "price": 90,
            "sizes": [
                {"value": "20", "active": True},
                {"value": "21", "active": True},
                {"value": "22", "active": True},
                {"value": "23", "active": True},
                {"value": "24", "active": True},
                {"value": "25", "active": True},
                {"value": "26", "active": True},
                {"value": "27", "active": False},
                {"value": "28", "active": True},
                {"value": "29", "active": False},
                {"value": "30", "active": True}
            ],
            "images": ["24-1.png", "24-2.png", "24-3.png", "24-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [25, 26, 27, 28, 29, 30]
        },

        {
            "id": 25,
            "title": "Nike Diamond Turf 93 TD",
            "slug": "Nike-Diamond-Turf-93-TD",
            "descriptionText": "The Nike Diamond Turf 93 TD is designed for young football players, combining comfort, grip, and durability for the field.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: ND1234-093"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": [],
            "price": 100,
            "sizes": [
                {"value": "20", "active": True},
                {"value": "21", "active": True},
                {"value": "22", "active": True},
                {"value": "23", "active": True},
                {"value": "24", "active": True},
                {"value": "25", "active": True},
                {"value": "26", "active": True},
                {"value": "27", "active": False},
                {"value": "28", "active": True},
                {"value": "29", "active": False},
                {"value": "30", "active": True}
            ],
            "images": ["25-1.png", "25-2.png", "25-3.png", "25-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [24, 26, 27, 28, 29, 30]
        },

        {
            "id": 26,
            "title": "Jordan 1 Mid TD",
            "slug": "Jordan-1-Mid-TD",
            "descriptionText": "The Jordan 1 Mid TD is designed for young football players, combining style and comfort for the field.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: J125-001"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#000000", "#CE2029", "#F5F5DC"],
            "price": 95,
            "sizes": [
                {"value": "20", "active": True},
                {"value": "21", "active": True},
                {"value": "22", "active": True},
                {"value": "23", "active": True},
                {"value": "24", "active": True},
                {"value": "25", "active": True},
                {"value": "26", "active": True},
                {"value": "27", "active": False},
                {"value": "28", "active": True},
                {"value": "29", "active": False},
                {"value": "30", "active": True}
            ],
            "images": ["26-1.png", "26-2.png", "26-3.png", "26-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [24, 25, 27, 28, 29, 30]
        },

        {
            "id": 27,
            "title": "Nike Vapor Edge 360 \"Untouchable\"",
            "slug": "Nike-Vapor-Edge-360-Untouchable",
            "descriptionText": "The Nike Vapor Edge 360 \"Untouchable\" is built for football, offering grip, comfort, and support for the field.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: NV360-027"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": [],
            "price": 185,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["27-1.png", "27-2.png", "27-3.png", "27-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [24, 25, 26, 28, 29, 30]
        },

        {
            "id": 28,
            "title": "Nike Vapor Pro 1",
            "slug": "Nike-Vapor-Pro-1",
            "descriptionText": "The Nike Vapor Pro 1 is built for football, offering comfort, traction, and support on the field.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: NVP1234-001"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#000000", "#CE2029", "#F5F5DC"],
            "price": 190,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["28-1.png", "28-2.png", "28-3.png", "28-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [24, 25, 26, 27, 29, 30]
        },

        {
            "id": 29,
            "title": "Nike Alpha Menace Strong",
            "slug": "Nike-Alpha-Menace-Strong",
            "descriptionText": "The Nike Alpha Menace Strong is built for football, giving support and grip on the field while keeping a sleek look.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: NA1234-001"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#000000", "#4169E1", "#556B2F", "#800020"],
            "price": 175,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["29-1.png", "29-2.png", "29-3.png", "29-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [24, 25, 26, 27, 28, 30]
        },

        {
            "id": 30,
            "title": "Jordan Stadium 90 Low TD",
            "slug": "Jordan-Stadium-90-Low-TD",
            "descriptionText": "The Jordan Stadium 90 Low TD is designed for young football players, giving comfort and support on the field.",
            "descriptionOptions": ["Shown: Black/Crimson/Beige", "Style: JS90-001"],
            "categories": ["Football"],
            "genders": ["Men", "Women", "Kids"],
            "colors": ["#F5F5DC", "#CE2029", "#001F54", "#556B2F", "#000000"],
            "price": 95,
            "sizes": [
                {"value": "20", "active": True},
                {"value": "21", "active": True},
                {"value": "22", "active": True},
                {"value": "23", "active": True},
                {"value": "24", "active": True},
                {"value": "25", "active": True},
                {"value": "26", "active": True},
                {"value": "27", "active": False},
                {"value": "28", "active": True},
                {"value": "29", "active": False},
                {"value": "30", "active": True}
            ],
            "images": ["30-1.png", "30-2.png", "30-3.png", "30-4.png"],
            "review": 4,
            "isNewRelease": True,
            "similarProducts": [24, 25, 26, 27, 28, 29]
        },

        {
            "id": 31,
            "title": "Nike Victory Pro 4",
            "slug": "Nike-Victory-Pro-4",
            "descriptionText": "The Nike Victory Pro 4 is designed for golfers, combining stability and comfort for long hours on the course.",
            "descriptionOptions": ["Shown: Navy/Beige/Maroon", "Style: NV31-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#001F54", "#F5F5DC", "#800020"],
            "price": 180,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["31-1.png", "31-2.png", "31-3.png", "31-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [32, 33, 34, 35, 36, 37, 38]
        },

        {
            "id": 32,
            "title": "Nike Air Max 90 G",
            "slug": "Nike-Air-Max-90-G",
            "descriptionText": "The Nike Air Max 90 G delivers comfort and stability on the golf course with a stylish, supportive design.",
            "descriptionOptions": ["Shown: Olive/Navy/Maroon", "Style: NAM90G-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#556B2F", "#001F54", "#800020"],
            "price": 175,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["32-1.png", "32-2.png", "32-3.png", "32-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 33, 34, 35, 36, 37, 38]
        },

        {
            "id": 33,
            "title": "Nike Victory Tour 4",
            "slug": "Nike-Victory-Tour-4",
            "descriptionText": "The Nike Victory Tour 4 offers comfort, stability, and style for golfers, helping maintain performance on the course.",
            "descriptionOptions": ["Shown: Royal/Olive/Maroon", "Style: NVT4-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#4169E1", "#556B2F", "#800020"],
            "price": 185,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["33-1.png", "33-2.png", "33-3.png", "33-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 34, 35, 36, 37, 38]
        },

        {
            "id": 34,
            "title": "Jordan NU Retro 1 G",
            "slug": "Jordan-NU-Retro-1-G",
            "descriptionText": "The Jordan NU Retro 1 G is designed for golf, providing comfort and stability on the course with a stylish look.",
            "descriptionOptions": ["Shown: Maroon/Beige/Navy", "Style: JN1G-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#800020", "#F5F5DC", "#001F54"],
            "price": 190,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["34-1.png", "34-2.png", "34-3.png", "34-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 33, 35, 36, 37, 38]
        },

        {
            "id": 35,
            "title": "Jordan Air Rev",
            "slug": "Jordan-Air-Rev",
            "descriptionText": "The Jordan Air Rev is designed for golf, providing stability, comfort, and style on the course.",
            "descriptionOptions": ["Shown: Beige/Olive/Navy", "Style: JAR-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#F5F5DC", "#556B2F", "#001F54"],
            "price": 185,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["35-1.png", "35-2.png", "35-3.png", "35-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 33, 34, 36, 37, 38]
        },

        {
            "id": 36,
            "title": "Air Pegasus '89 G",
            "slug": "Air-Pegasus-89-G",
            "descriptionText": "The Air Pegasus '89 G delivers comfort and stability for golfers, keeping you supported during your rounds.",
            "descriptionOptions": ["Shown: Maroon/Navy/Olive", "Style: AP89G-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#800020", "#001F54", "#556B2F"],
            "price": 180,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["36-1.png", "36-2.png", "36-3.png", "36-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 33, 34, 35, 37, 38]
        },

        {
            "id": 37,
            "title": "Air Jordan Mule",
            "slug": "Air-Jordan-Mule",
            "descriptionText": "The Air Jordan Mule is designed for golf, offering easy slip-on comfort and stability for the course.",
            "descriptionOptions": ["Shown: Navy/Beige/Crimson", "Style: AJM-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#001F54", "#F5F5DC", "#CE2029"],
            "price": 170,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["37-1.png", "37-2.png", "37-3.png", "37-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 33, 34, 35, 36, 38]
        },

        {
            "id": 38,
            "title": "Air Jordan 1 Low G",
            "slug": "Air-Jordan-1-Low-G",
            "descriptionText": "The Air Jordan 1 Low G provides golfers with comfort, stability, and a stylish design for the course.",
            "descriptionOptions": ["Shown: Olive/Beige/Blue", "Style: AJ1LG-001"],
            "categories": ["Golf"],
            "genders": ["Men"],
            "colors": ["#556B2F", "#F5F5DC", "#001F54"],
            "price": 185,
            "sizes": [
                {"value": "38", "active": True},
                {"value": "39", "active": True},
                {"value": "40", "active": True},
                {"value": "41", "active": True},
                {"value": "42", "active": True},
                {"value": "43", "active": True},
                {"value": "44", "active": True},
                {"value": "45", "active": False},
                {"value": "46", "active": True},
                {"value": "47", "active": False},
                {"value": "48", "active": True}
            ],
            "images": ["38-1.png", "38-2.png", "38-3.png", "38-4.png"],
            "review": 5,
            "isNewRelease": True,
            "similarProducts": [31, 32, 33, 34, 35, 36, 37]
        }
    ]

    for p in TEST_PRODUCTS:
        product, created = Product.objects.get_or_create(
            id=p['id'],
            defaults={
                'title': p['title'],
                'slug': p['slug'],
                'description_text': p['descriptionText'],
                'price': p['price'],
                'review': p['review'],
                'is_new_release': p['isNewRelease']
            }
        )

        for c in p['categories']:
            category_obj, _ = Category.objects.get_or_create(name=c)
            product.categories.add(category_obj)



        for s in p['sizes']:
            ProductSize.objects.update_or_create(
                product=product,
                value=s['value'],
                defaults={'active': s['active']}
            )

    return JsonResponse({'status': 'success', 'message': 'Test products created'})



class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff



class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductListSerializer
    pagination_class = ProductPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description_text', 'categories', 'genders']
    ordering_fields = ['price', 'review', 'id']
    ordering = ['-id']


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductDetailSerializer




class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"




class ProductCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        categories = set()
        for product in Product.objects.all():
            categories.update(product.Category.name or [])

        return Response({"categories": list(categories)})



class ProductFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()

        sizes = self.request.query_params.getlist('size')
        colors = self.request.query_params.getlist('color')
        categories = self.request.query_params.getlist('category')
        genders = self.request.query_params.getlist('gender')
        sort = self.request.query_params.get('sort', 'id')

        if sizes:
            qs = qs.filter(sizes__value__in=sizes)
        if colors:
            qs = qs.filter(colors__name__in=colors)
        if categories:
            qs = qs.filter(categories__contains=categories)
        if genders:
            qs = qs.filter(genders__contains=genders)

        qs = qs.order_by(sort).distinct()
        return qs



class ProductSlugsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSlugSerializer(products, many=True)
        return Response(serializer.data)




class SimilarProductsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 20



class SimilarProductsView(generics.ListAPIView):
    serializer_class = ProductMinimalSerializer
    pagination_class = SimilarProductsPagination

    def get_queryset(self , limit=5):
        product_slug = self.kwargs["slug"]
        product = Product.objects.get(slug=product_slug)
        return Product.objects.filter(categories__in=product.categories.all()).exclude(slug=product.slug).distinct()[:limit]


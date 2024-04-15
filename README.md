# Hotels Data Merge Application #

This is an application that takes in data from multiple suppliers, compiles and presents the data is easy to read format.

### Prerequisites ###
You need to have the following installed to run this application:
* Python 3
* Django

### How to run ###
You can run this server by running the following command: `make run`

This will run the application on your local machine on port 8000.

### APIs ###

#### Get hotels by id ####
This returns hotels by hotel id. You can pass in a list of hotel_ids and you should get back a list of hotel details.

```commandline
curl --location 'localhost:8000/hotels/search' \
--header 'Content-Type: application/json' \
--data '{
    "hotel_ids": ["iJhz"]
}'
```

Sample response:
```json
{
    "resp": [
        {
            "id": "iJhz",
            "destination_id": 5432,
            "name": "Beach Villas Singapore",
            "latitude": 1.264751,
            "longitude": 103.824006,
            "address": "8 Sentosa Gateway, Beach Villas, 098269",
            "city": "Singapore",
            "country": "Singapore",
            "description": "This 5 star hotel is located on the coastline of Singapore. Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA. Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station. Featuring sundecks and pool, garden or sea views, the plush 1- to 3-bedroom villas offer free Wi-Fi and flat-screens, as well as free-standing baths, minibars, and tea and coffeemaking facilities. Upgraded villas add private pools, fridges and microwaves; some have wine cellars. A 4-bedroom unit offers a kitchen and a living room. There's 24-hour room and butler service. Amenities include posh restaurant, plus an outdoor pool, a hot tub, and free parking.",
            "facilities": [
                "Kettle",
                "Outdoor pool",
                "Wifi",
                "Iron",
                "Coffee machine",
                "Tv",
                "Hair dryer",
                "Tub",
                "Business center",
                "Indoor pool",
                "Breakfast",
                "Drycleaning",
                "Aircon",
                "Pool",
                "Childcare"
            ],
            "booking_conditions": [
                "Guests are required to show a photo identification and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Payment before arrival via bank transfer is required. The property will contact you after you book to provide instructions. Please note that the full amount of the reservation is due before arrival. Resorts World Sentosa will send a confirmation with detailed payment information. After full payment is taken, the property's details, including the address and where to collect keys, will be emailed to you. Bag checks will be conducted prior to entry to Adventure Cove Waterpark. === Upon check-in, guests will be provided with complimentary Sentosa Pass (monorail) to enjoy unlimited transportation between Sentosa Island and Harbour Front (VivoCity). === Prepayment for non refundable bookings will be charged by RWS Call Centre. === All guests can enjoy complimentary parking during their stay, limited to one exit from the hotel per day. === Room reservation charges will be charged upon check-in. Credit card provided upon reservation is for guarantee purpose. === For reservations made with inclusive breakfast, please note that breakfast is applicable only for number of adults paid in the room rate. Any children or additional adults are charged separately for breakfast and are to paid directly to the hotel.",
                "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
                "Pets are not allowed.",
                "WiFi is available in all areas and is free of charge.",
                "Free private parking is possible on site (reservation is not needed)."
            ],
            "images": {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "caption": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                        "caption": "Bathroom"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "caption": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg",
                        "caption": "Double room"
                    }
                ],
                "sites": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg",
                        "caption": "Front"
                    }
                ],
                "amenities": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                        "caption": "RWS"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                        "caption": "Sentosa Gateway"
                    }
                ]
            }
        }
    ],
    "error": ""
}
```

This only accepts a max limit of 500 hotel_ids. If passed in more than that, this will return 400.

#### Get hotels by destination id ####
This returns hotels by destination id. You can pass in a destination_id and you should get back a list of hotel details.

```commandline
curl --location 'localhost:8000/hotels/search' \
--header 'Content-Type: application/json' \
--data '{
    "destination_id": 5432
}'
```

Sample response:
```json
{
    "resp": [
        {
            "id": "iJhz",
            "destination_id": 5432,
            "name": "Beach Villas Singapore",
            "latitude": 1.264751,
            "longitude": 103.824006,
            "address": "8 Sentosa Gateway, Beach Villas, 098269",
            "city": "Singapore",
            "country": "Singapore",
            "description": "This 5 star hotel is located on the coastline of Singapore. Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA. Surrounded by tropical gardens, these upscale villas in elegant Colonial-style buildings are part of the Resorts World Sentosa complex and a 2-minute walk from the Waterfront train station. Featuring sundecks and pool, garden or sea views, the plush 1- to 3-bedroom villas offer free Wi-Fi and flat-screens, as well as free-standing baths, minibars, and tea and coffeemaking facilities. Upgraded villas add private pools, fridges and microwaves; some have wine cellars. A 4-bedroom unit offers a kitchen and a living room. There's 24-hour room and butler service. Amenities include posh restaurant, plus an outdoor pool, a hot tub, and free parking.",
            "facilities": [
                "Kettle",
                "Outdoor pool",
                "Wifi",
                "Iron",
                "Coffee machine",
                "Tv",
                "Hair dryer",
                "Tub",
                "Business center",
                "Indoor pool",
                "Breakfast",
                "Drycleaning",
                "Aircon",
                "Pool",
                "Childcare"
            ],
            "booking_conditions": [
                "Guests are required to show a photo identification and credit card upon check-in. Please note that all Special Requests are subject to availability and additional charges may apply. Payment before arrival via bank transfer is required. The property will contact you after you book to provide instructions. Please note that the full amount of the reservation is due before arrival. Resorts World Sentosa will send a confirmation with detailed payment information. After full payment is taken, the property's details, including the address and where to collect keys, will be emailed to you. Bag checks will be conducted prior to entry to Adventure Cove Waterpark. === Upon check-in, guests will be provided with complimentary Sentosa Pass (monorail) to enjoy unlimited transportation between Sentosa Island and Harbour Front (VivoCity). === Prepayment for non refundable bookings will be charged by RWS Call Centre. === All guests can enjoy complimentary parking during their stay, limited to one exit from the hotel per day. === Room reservation charges will be charged upon check-in. Credit card provided upon reservation is for guarantee purpose. === For reservations made with inclusive breakfast, please note that breakfast is applicable only for number of adults paid in the room rate. Any children or additional adults are charged separately for breakfast and are to paid directly to the hotel.",
                "All children are welcome. One child under 12 years stays free of charge when using existing beds. One child under 2 years stays free of charge in a child's cot/crib. One child under 4 years stays free of charge when using existing beds. One older child or adult is charged SGD 82.39 per person per night in an extra bed. The maximum number of children's cots/cribs in a room is 1. There is no capacity for extra beds in the room.",
                "Pets are not allowed.",
                "WiFi is available in all areas and is free of charge.",
                "Free private parking is possible on site (reservation is not needed)."
            ],
            "images": {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "caption": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                        "caption": "Bathroom"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                        "caption": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/3.jpg",
                        "caption": "Double room"
                    }
                ],
                "sites": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/1.jpg",
                        "caption": "Front"
                    }
                ],
                "amenities": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                        "caption": "RWS"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                        "caption": "Sentosa Gateway"
                    }
                ]
            }
        },
        {
            "id": "SjyX",
            "destination_id": 5432,
            "name": "InterContinental Singapore Robertson Quay",
            "latitude": null,
            "longitude": null,
            "address": "1 Nanson Rd, Singapore 238909",
            "city": "Singapore",
            "country": "Singapore",
            "description": "Enjoy sophisticated waterfront living at the new InterContinental® Singapore Robertson Quay, luxury's preferred address nestled in the heart of Robertson Quay along the Singapore River, with the CBD just five minutes drive away. Magnifying the comforts of home, each of our 225 studios and suites features a host of thoughtful amenities that combine modernity with elegance, whilst maintaining functional practicality. The hotel also features a chic, luxurious Club InterContinental Lounge. InterContinental Singapore Robertson Quay is luxury's preferred address offering stylishly cosmopolitan riverside living for discerning travelers to Singapore. Prominently situated along the Singapore River, the 225-room inspiring luxury hotel is easily accessible to the Marina Bay Financial District, Central Business District, Orchard Road and Singapore Changi International Airport, all located a short drive away. The hotel features the latest in Club InterContinental design and service experience, and five dining options including Publico, an Italian landmark dining and entertainment destination by the waterfront.",
            "facilities": [
                "Minibar",
                "Outdoor pool",
                "Parking",
                "Wifi",
                "Dry cleaning",
                "Tv",
                "Pool",
                "Hair dryer",
                "Business center",
                "Bathtub",
                "Bar",
                "Breakfast",
                "Aircon",
                "Concierge",
                "Childcare"
            ],
            "booking_conditions": [],
            "images": {
                "rooms": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i93_m.jpg",
                        "caption": "Double room"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i94_m.jpg",
                        "caption": "Bathroom"
                    }
                ],
                "sites": [
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i1_m.jpg",
                        "caption": "Restaurant"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i2_m.jpg",
                        "caption": "Hotel Exterior"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i5_m.jpg",
                        "caption": "Entrance"
                    },
                    {
                        "url": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i24_m.jpg",
                        "caption": "Bar"
                    }
                ],
                "amenities": []
            }
        }
    ],
    "error": ""
}
```

This assumes that the destination_id being passed in is an integer.

### Future Improvements ###
The following are planned improvements:
* Make calls to suppliers concurrent
* Add from and size to paginate the response
* Get supplier urls from environment instead of hardcoding in code

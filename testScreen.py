# https://api.dexscreener.com/latest/dex/search/?q=:q
import requests

# requests = requests.get('https://api.dexscreener.io/latest/dex/tokens/0x2170Ed0880ac9A755fd29B2688956BD959F933F8')
requests = requests.get('https://dexscreener.com/new-pairs?rankBy=pairAge&order=asc')
print(requests.text)

'''
{
	"schemaVersion": "1.0.0",
	"pairs": [{
		"chainId": "sui",
		"dexId": "flowx",
		"url": "https://dexscreener.com/sui/0xe5b3c4f85a2ec7507c70d5111159e8d7e4c8b401ae9f346010d491dacbaa28d0",
		"pairAddress": "0xe5b3c4f85a2ec7507c70d5111159e8d7e4c8b401ae9f346010d491dacbaa28d0",
		"baseToken": {
			"address": "0xc3e1a1b98a68aef0d73a6c2bb615b7186004c4367c61df7e8292ae375785272c::qingge::QINGGE",
			"name": "qingge",
			"symbol": "QINGGE"
		},
		"quoteToken": {
			"address": "0x2::sui::SUI",
			"name": "Sui",
			"symbol": "SUI"
		},
		"priceNative": "0.01191",
		"priceUsd": "0.02319",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 0
			},
			"h24": {
				"buys": 2,
				"sells": 0
			}
		},
		"volume": {
			"h24": 0.02,
			"h6": 0,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": 0,
			"h24": 0.52
		},
		"liquidity": {
			"usd": 4.26,
			"base": 91.952,
			"quote": 1.09584
		},
		"fdv": 487172,
		"pairCreatedAt": 1709880855000
	}]
}


{
	"schemaVersion": "1.0.0",
	"pairs": [{
		"chainId": "bsc",
		"dexId": "uniswap",
		"url": "https://dexscreener.com/bsc/0xb125aa15ad943d96e813e4a06d0c34716f897e26",
		"pairAddress": "0xb125aa15Ad943D96e813E4A06d0c34716F897e26",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3286.3490",
		"priceUsd": "3286.34",
		"txns": {
			"m5": {
				"buys": 10,
				"sells": 17
			},
			"h1": {
				"buys": 168,
				"sells": 139
			},
			"h6": {
				"buys": 940,
				"sells": 779
			},
			"h24": {
				"buys": 3638,
				"sells": 3283
			}
		},
		"volume": {
			"h24": 13531528.88,
			"h6": 2382014.65,
			"h1": 460058.32,
			"m5": 12076.23
		},
		"priceChange": {
			"m5": -0.46,
			"h1": -0.98,
			"h6": -2.86,
			"h24": -7.38
		},
		"liquidity": {
			"usd": 674263.7,
			"base": 193.3707,
			"quote": 38779
		},
		"fdv": 1988190569,
		"pairCreatedAt": 1705727210000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0xd0e226f674bbf064f54ab47f42473ff80db98cba",
		"pairAddress": "0xD0e226f674bBf064f54aB47F42473fF80DB98CBA",
		"labels": ["v3"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9565",
		"priceUsd": "3287.63",
		"txns": {
			"m5": {
				"buys": 8,
				"sells": 15
			},
			"h1": {
				"buys": 151,
				"sells": 141
			},
			"h6": {
				"buys": 759,
				"sells": 749
			},
			"h24": {
				"buys": 3488,
				"sells": 3127
			}
		},
		"volume": {
			"h24": 22341889.77,
			"h6": 4523298.53,
			"h1": 777311.73,
			"m5": 53067.48
		},
		"priceChange": {
			"m5": -0.35,
			"h1": -0.96,
			"h6": -2.77,
			"h24": -7.34
		},
		"liquidity": {
			"usd": 5133195.21,
			"base": 1134.5271,
			"quote": 2542.4792
		},
		"fdv": 1988969084,
		"pairCreatedAt": 1680536288000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0x539e0ebfffd39e54a0f7e5f8fec40ade7933a664",
		"pairAddress": "0x539e0EBfffd39e54A0f7E5F8FEc40ade7933A664",
		"labels": ["v3"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
			"name": "USD Coin",
			"symbol": "USDC"
		},
		"priceNative": "3286.6775",
		"priceUsd": "3286.67",
		"txns": {
			"m5": {
				"buys": 4,
				"sells": 13
			},
			"h1": {
				"buys": 55,
				"sells": 64
			},
			"h6": {
				"buys": 411,
				"sells": 477
			},
			"h24": {
				"buys": 1801,
				"sells": 1851
			}
		},
		"volume": {
			"h24": 5294519.2,
			"h6": 357151.45,
			"h1": 41943.63,
			"m5": 4523.62
		},
		"priceChange": {
			"m5": -0.39,
			"h1": -0.97,
			"h6": -2.9,
			"h24": -7.42
		},
		"liquidity": {
			"usd": 876174.36,
			"base": 158.467,
			"quote": 355344
		},
		"fdv": 1988389312,
		"pairCreatedAt": 1680356039000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0xbe141893e4c6ad9272e8c04bab7e6a10604501a5",
		"pairAddress": "0xBe141893E4c6AD9272e8C04BAB7E6a10604501a5",
		"labels": ["v3"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3289.1416",
		"priceUsd": "3289.14",
		"txns": {
			"m5": {
				"buys": 9,
				"sells": 18
			},
			"h1": {
				"buys": 117,
				"sells": 125
			},
			"h6": {
				"buys": 800,
				"sells": 762
			},
			"h24": {
				"buys": 2744,
				"sells": 2650
			}
		},
		"volume": {
			"h24": 11544132.35,
			"h6": 2500474.03,
			"h1": 540760.97,
			"m5": 37532.08
		},
		"priceChange": {
			"m5": -0.32,
			"h1": -0.93,
			"h6": -2.76,
			"h24": -7.33
		},
		"liquidity": {
			"usd": 1192762.28,
			"base": 288.7056,
			"quote": 243168
		},
		"fdv": 1989880077,
		"pairCreatedAt": 1681214432000
	}, {
		"chainId": "bsc",
		"dexId": "thena",
		"url": "https://dexscreener.com/bsc/0x1123e75b71019962cd4d21b0f3018a6412edb63c",
		"pairAddress": "0x1123E75b71019962CD4d21b0F3018a6412eDb63C",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9643",
		"priceUsd": "3294.85",
		"txns": {
			"m5": {
				"buys": 1,
				"sells": 7
			},
			"h1": {
				"buys": 19,
				"sells": 26
			},
			"h6": {
				"buys": 112,
				"sells": 172
			},
			"h24": {
				"buys": 622,
				"sells": 545
			}
		},
		"volume": {
			"h24": 15441554.59,
			"h6": 2411399.1,
			"h1": 367679.1,
			"m5": 30405.1
		},
		"priceChange": {
			"m5": 0.3,
			"h1": -0.27,
			"h6": -2.63,
			"h24": -6.86
		},
		"liquidity": {
			"usd": 7281271.76,
			"base": 1140.7098,
			"quote": 6376.9084
		},
		"fdv": 1993338622
	}, {
		"chainId": "bsc",
		"dexId": "uniswap",
		"url": "https://dexscreener.com/bsc/0x0f338ec12d3f7c3d77a4b9fcc1f95f3fb6ad0ea6",
		"pairAddress": "0x0f338Ec12d3f7C3D77A4B9fcC1f95F3FB6AD0EA6",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9559",
		"priceUsd": "3290.33",
		"txns": {
			"m5": {
				"buys": 4,
				"sells": 11
			},
			"h1": {
				"buys": 84,
				"sells": 104
			},
			"h6": {
				"buys": 518,
				"sells": 526
			},
			"h24": {
				"buys": 2026,
				"sells": 1929
			}
		},
		"volume": {
			"h24": 2441233.79,
			"h6": 713022.13,
			"h1": 141775.97,
			"m5": 8298.58
		},
		"priceChange": {
			"m5": -0.05,
			"h1": -0.93,
			"h6": -2.87,
			"h24": -7.1
		},
		"liquidity": {
			"usd": 1456881.27,
			"base": 332.267,
			"quote": 658.1777
		},
		"fdv": 1990604380,
		"pairCreatedAt": 1678911207000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0xd4dca84e1808da3354924cd243c66828cf775470",
		"pairAddress": "0xD4dCA84E1808da3354924cD243c66828cf775470",
		"labels": ["v3"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
			"name": "BTCB Token",
			"symbol": "BTCB"
		},
		"priceNative": "0.05045",
		"priceUsd": "3283.92",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 9,
				"sells": 0
			},
			"h6": {
				"buys": 110,
				"sells": 60
			},
			"h24": {
				"buys": 341,
				"sells": 234
			}
		},
		"volume": {
			"h24": 5654010.21,
			"h6": 1726105.69,
			"h1": 58340.06,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -0.63,
			"h6": -2.64,
			"h24": -7.53
		},
		"liquidity": {
			"usd": 37805785.62,
			"base": 7042.7665,
			"quote": 225.5033
		},
		"fdv": 1986725923,
		"pairCreatedAt": 1680355343000
	}, {
		"chainId": "bsc",
		"dexId": "thena",
		"url": "https://dexscreener.com/bsc/0xa60a504d92a1c95bda729c3f745b361ca822d6dd",
		"pairAddress": "0xa60a504d92a1C95bda729C3F745B361cA822d6dd",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3286.3848",
		"priceUsd": "3286.38",
		"txns": {
			"m5": {
				"buys": 3,
				"sells": 10
			},
			"h1": {
				"buys": 16,
				"sells": 37
			},
			"h6": {
				"buys": 185,
				"sells": 217
			},
			"h24": {
				"buys": 664,
				"sells": 713
			}
		},
		"volume": {
			"h24": 3001492.48,
			"h6": 900744.89,
			"h1": 112760.63,
			"m5": 28765.29
		},
		"priceChange": {
			"m5": -0.36,
			"h1": -1.04,
			"h6": -2.82,
			"h24": -7.49
		},
		"liquidity": {
			"usd": 920975.25,
			"base": 147.1471,
			"quote": 437393
		},
		"fdv": 1988212249
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0x74e4716e431f45807dcf19f284c7aa99f18a4fbc",
		"pairAddress": "0x74E4716E431f45807DCF19f284c7aA99F18a4fbc",
		"labels": ["v2"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9600",
		"priceUsd": "3292.64",
		"txns": {
			"m5": {
				"buys": 8,
				"sells": 4
			},
			"h1": {
				"buys": 46,
				"sells": 57
			},
			"h6": {
				"buys": 278,
				"sells": 272
			},
			"h24": {
				"buys": 1217,
				"sells": 1226
			}
		},
		"volume": {
			"h24": 807564.14,
			"h6": 150765.95,
			"h1": 21602.79,
			"m5": 1600.31
		},
		"priceChange": {
			"m5": 0.15,
			"h1": -0.85,
			"h6": -2.86,
			"h24": -7.02
		},
		"liquidity": {
			"usd": 4290627.42,
			"base": 651.548,
			"quote": 3883.2727
		},
		"fdv": 1991997030
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0x531febfeb9a61d948c384acfbe6dcc51057aea7e",
		"pairAddress": "0x531FEbfeb9a61D948c384ACFBe6dCc51057AEa7e",
		"labels": ["v2"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3290.4924",
		"priceUsd": "3290.49",
		"txns": {
			"m5": {
				"buys": 4,
				"sells": 5
			},
			"h1": {
				"buys": 52,
				"sells": 34
			},
			"h6": {
				"buys": 202,
				"sells": 183
			},
			"h24": {
				"buys": 872,
				"sells": 656
			}
		},
		"volume": {
			"h24": 355381.5,
			"h6": 82594.32,
			"h1": 18604.85,
			"m5": 2988.13
		},
		"priceChange": {
			"m5": -0.08,
			"h1": -1.08,
			"h6": -2.73,
			"h24": -7.43
		},
		"liquidity": {
			"usd": 1531784.99,
			"base": 232.7592,
			"quote": 765892
		},
		"fdv": 1990697261,
		"pairCreatedAt": 1619277331000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0x7d05c84581f0c41ad80ddf677a510360bae09a5a",
		"pairAddress": "0x7d05c84581f0C41AD80ddf677A510360bae09a5A",
		"labels": ["v3"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9664",
		"priceUsd": "3292.13",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 1
			},
			"h1": {
				"buys": 36,
				"sells": 7
			},
			"h6": {
				"buys": 49,
				"sells": 90
			},
			"h24": {
				"buys": 257,
				"sells": 305
			}
		},
		"volume": {
			"h24": 1091037.67,
			"h6": 165515.63,
			"h1": 38282.68,
			"m5": 3551.01
		},
		"priceChange": {
			"m5": -0.28,
			"h1": -0.61,
			"h6": -2.43,
			"h24": -7.37
		},
		"liquidity": {
			"usd": 5540237.43,
			"base": 1056.1685,
			"quote": 3739.2023
		},
		"fdv": 1991690097,
		"pairCreatedAt": 1680355748000
	}, {
		"chainId": "bsc",
		"dexId": "biswap",
		"url": "https://dexscreener.com/bsc/0x63b30de1a998e9e64fd58a21f68d323b9bcd8f85",
		"pairAddress": "0x63b30de1A998e9E64FD58A21F68D323B9BcD8F85",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3290.8169",
		"priceUsd": "3290.81",
		"txns": {
			"m5": {
				"buys": 3,
				"sells": 6
			},
			"h1": {
				"buys": 14,
				"sells": 22
			},
			"h6": {
				"buys": 81,
				"sells": 102
			},
			"h24": {
				"buys": 364,
				"sells": 316
			}
		},
		"volume": {
			"h24": 481459.82,
			"h6": 81609.56,
			"h1": 16150.09,
			"m5": 4349.84
		},
		"priceChange": {
			"m5": -0.12,
			"h1": -0.71,
			"h6": -2.72,
			"h24": -7.43
		},
		"liquidity": {
			"usd": 3335658.85,
			"base": 506.8131,
			"quote": 1667829
		},
		"fdv": 1990893595,
		"pairCreatedAt": 1621793962000
	}, {
		"chainId": "bsc",
		"dexId": "orion",
		"url": "https://dexscreener.com/bsc/0x21fb1e55ac7f1d205f18a3f7b37b63db4da5b628",
		"pairAddress": "0x21Fb1e55AC7F1d205f18A3F7b37b63DB4dA5b628",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3293.4184",
		"priceUsd": "3293.41",
		"txns": {
			"m5": {
				"buys": 2,
				"sells": 1
			},
			"h1": {
				"buys": 4,
				"sells": 10
			},
			"h6": {
				"buys": 32,
				"sells": 52
			},
			"h24": {
				"buys": 152,
				"sells": 159
			}
		},
		"volume": {
			"h24": 251715.84,
			"h6": 45674.77,
			"h1": 6176.6,
			"m5": 1180.35
		},
		"priceChange": {
			"m5": 0.07,
			"h1": -0.54,
			"h6": -2.49,
			"h24": -7.18
		},
		"liquidity": {
			"usd": 2732447.52,
			"base": 414.8345,
			"quote": 1366223
		},
		"fdv": 1992467479,
		"pairCreatedAt": 1648016406000
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0x70d8929d04b60af4fb9b58713ebcf18765ade422",
		"pairAddress": "0x70D8929d04b60Af4fb9B58713eBcf18765aDE422",
		"labels": ["v1"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9711",
		"priceUsd": "3298.83",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 2
			},
			"h1": {
				"buys": 4,
				"sells": 9
			},
			"h6": {
				"buys": 33,
				"sells": 32
			},
			"h24": {
				"buys": 129,
				"sells": 143
			}
		},
		"volume": {
			"h24": 20562.45,
			"h6": 3551.65,
			"h1": 462.8,
			"m5": 9.56
		},
		"priceChange": {
			"m5": 0.36,
			"h1": -0.39,
			"h6": -2.49,
			"h24": -6.8
		},
		"liquidity": {
			"usd": 519497.9,
			"base": 78.7396,
			"quote": 470.165
		},
		"fdv": 1995744373
	}, {
		"chainId": "bsc",
		"dexId": "pancakeswap",
		"url": "https://dexscreener.com/bsc/0xea26b78255df2bbc31c1ebf60010d78670185bd0",
		"pairAddress": "0xEa26B78255Df2bBC31C1eBf60010D78670185bD0",
		"labels": ["v2"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
			"name": "USD Coin",
			"symbol": "USDC"
		},
		"priceNative": "3292.09744",
		"priceUsd": "3292.097",
		"txns": {
			"m5": {
				"buys": 1,
				"sells": 1
			},
			"h1": {
				"buys": 2,
				"sells": 12
			},
			"h6": {
				"buys": 42,
				"sells": 55
			},
			"h24": {
				"buys": 155,
				"sells": 163
			}
		},
		"volume": {
			"h24": 65661.54,
			"h6": 31957.67,
			"h1": 2537.57,
			"m5": 451.39
		},
		"priceChange": {
			"m5": 0.04,
			"h1": -0.84,
			"h6": -2.68,
			"h24": -7.4
		},
		"liquidity": {
			"usd": 559107.58,
			"base": 84.9166,
			"quote": 279553
		},
		"fdv": 1991668287,
		"pairCreatedAt": 1619380346000
	}, {
		"chainId": "bsc",
		"dexId": "uniswap",
		"url": "https://dexscreener.com/bsc/0x17507bef4c3abc1bc715be723ee1baf571256e05",
		"pairAddress": "0x17507bEF4c3abC1Bc715be723eE1baF571256E05",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
			"name": "USD Coin",
			"symbol": "USDC"
		},
		"priceNative": "3294.3526",
		"priceUsd": "3294.35",
		"txns": {
			"m5": {
				"buys": 1,
				"sells": 1
			},
			"h1": {
				"buys": 1,
				"sells": 5
			},
			"h6": {
				"buys": 11,
				"sells": 27
			},
			"h24": {
				"buys": 102,
				"sells": 102
			}
		},
		"volume": {
			"h24": 82799.4,
			"h6": 5107.59,
			"h1": 952.48,
			"m5": 443.51
		},
		"priceChange": {
			"m5": 0.06,
			"h1": -0.64,
			"h6": -2.62,
			"h24": -7.31
		},
		"liquidity": {
			"usd": 284468.63,
			"base": 18.2115,
			"quote": 224473
		},
		"fdv": 1993032665,
		"pairCreatedAt": 1678735471000
	}, {
		"chainId": "bsc",
		"dexId": "biswap",
		"url": "https://dexscreener.com/bsc/0x5bf6941f029424674bb93a43b79fc46bf4a67c21",
		"pairAddress": "0x5bf6941f029424674bb93A43b79fc46bF4A67c21",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9671",
		"priceUsd": "3284.49",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 2,
				"sells": 2
			},
			"h6": {
				"buys": 16,
				"sells": 20
			},
			"h24": {
				"buys": 73,
				"sells": 73
			}
		},
		"volume": {
			"h24": 19268.52,
			"h6": 3112.73,
			"h1": 329.1,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -1.05,
			"h6": -2.84,
			"h24": -7.14
		},
		"liquidity": {
			"usd": 508562.62,
			"base": 77.4186,
			"quote": 461.9674
		},
		"fdv": 1987070841,
		"pairCreatedAt": 1622011937000
	}, {
		"chainId": "bsc",
		"dexId": "nomiswap",
		"url": "https://dexscreener.com/bsc/0x13de257cb86a08753df938b6ad30d1a456a863e6",
		"pairAddress": "0x13dE257cb86a08753Df938b6ad30d1A456A863e6",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9604",
		"priceUsd": "3280.85",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 5,
				"sells": 6
			},
			"h6": {
				"buys": 24,
				"sells": 31
			},
			"h24": {
				"buys": 111,
				"sells": 119
			}
		},
		"volume": {
			"h24": 20919.6,
			"h6": 4148.34,
			"h1": 440.62,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -1.06,
			"h6": -3.17,
			"h24": -7.32
		},
		"liquidity": {
			"usd": 135855.65,
			"base": 20.7043,
			"quote": 123.408
		},
		"fdv": 1984865200,
		"pairCreatedAt": 1642009124000
	}, {
		"chainId": "bsc",
		"dexId": "apeswap",
		"url": "https://dexscreener.com/bsc/0xa0c3ef24414ed9c9b456740128d8e63d016a9e11",
		"pairAddress": "0xA0C3Ef24414ED9C9B456740128d8E63D016A9e11",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9705",
		"priceUsd": "3286.59",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 2,
				"sells": 1
			},
			"h6": {
				"buys": 10,
				"sells": 13
			},
			"h24": {
				"buys": 94,
				"sells": 76
			}
		},
		"volume": {
			"h24": 4870.89,
			"h6": 706.28,
			"h1": 106.98,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -0.49,
			"h6": -2.75,
			"h24": -7.14
		},
		"liquidity": {
			"usd": 132485.46,
			"base": 20.1554,
			"quote": 120.339
		},
		"fdv": 1988339916
	}, {
		"chainId": "bsc",
		"dexId": "mdex",
		"url": "https://dexscreener.com/bsc/0x0fb881c078434b1c0e4d0b64d8c64d12078b7ce2",
		"pairAddress": "0x0FB881c078434b1C0E4d0B64d8c64d12078b7Ce2",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3293.05741",
		"priceUsd": "3293.057",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 1,
				"sells": 2
			},
			"h6": {
				"buys": 9,
				"sells": 15
			},
			"h24": {
				"buys": 53,
				"sells": 55
			}
		},
		"volume": {
			"h24": 6170.55,
			"h6": 1451.4,
			"h1": 170.6,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -0.51,
			"h6": -2.43,
			"h24": -7.41
		},
		"liquidity": {
			"usd": 108865.54,
			"base": 16.5295,
			"quote": 54432
		},
		"fdv": 1992249053
	}, {
		"chainId": "bsc",
		"dexId": "0x571521f8c16f3c4eD5f2490f19187bA7A5A3CBDf",
		"url": "https://dexscreener.com/bsc/0x5de4c0980bcf4f78b3912eb9ef2e3be6c61fb7e5",
		"pairAddress": "0x5DE4c0980BcF4f78b3912eB9Ef2e3bE6c61fB7E5",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
			"name": "BUSD Token",
			"symbol": "BUSD"
		},
		"priceNative": "3295.1624",
		"priceUsd": "3295.16",
		"txns": {
			"m5": {
				"buys": 1,
				"sells": 0
			},
			"h1": {
				"buys": 1,
				"sells": 5
			},
			"h6": {
				"buys": 12,
				"sells": 24
			},
			"h24": {
				"buys": 65,
				"sells": 80
			}
		},
		"volume": {
			"h24": 46880.13,
			"h6": 10034.44,
			"h1": 1758.09,
			"m5": 368.31
		},
		"priceChange": {
			"m5": 0.22,
			"h1": -0.61,
			"h6": -2.36,
			"h24": -7.12
		},
		"liquidity": {
			"usd": 91772.33,
			"base": 24.583,
			"quote": 10767
		},
		"fdv": 1993522555,
		"pairCreatedAt": 1633838757000
	}, {
		"chainId": "bsc",
		"dexId": "iziswap",
		"url": "https://dexscreener.com/bsc/0x8b059170f5d4d85d13ae3cabd9b03abfbb2de829",
		"pairAddress": "0x8B059170F5d4D85D13aE3caBd9b03AbFbB2DE829",
		"labels": ["V2"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3588.09616",
		"priceUsd": "3588.096",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 0
			},
			"h24": {
				"buys": 0,
				"sells": 1
			}
		},
		"volume": {
			"h24": 0.02,
			"h6": 0,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": 0,
			"h24": 0
		},
		"liquidity": {
			"usd": 95872.21,
			"base": 0.2019,
			"quote": 95147
		},
		"fdv": 2170742958,
		"pairCreatedAt": 1697550325000
	}, {
		"chainId": "bsc",
		"dexId": "iziswap",
		"url": "https://dexscreener.com/bsc/0x3ae7e29860c0c10ca5bd234dee24e937e95e3c0e",
		"pairAddress": "0x3ae7E29860C0c10cA5bD234DEe24E937e95e3C0E",
		"labels": ["V2"],
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x14778860E937f509e651192a90589dE711Fb88a9",
			"name": "CyberConnect",
			"symbol": "CYBER"
		},
		"priceNative": "264.1037",
		"priceUsd": "3488.40",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 0
			},
			"h24": {
				"buys": 10,
				"sells": 0
			}
		},
		"volume": {
			"h24": 4357.18,
			"h6": 0,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": 0,
			"h24": 0.21
		},
		"liquidity": {
			"usd": 79962.27,
			"base": 16.9119,
			"quote": 1587.3607
		},
		"fdv": 2110432791,
		"pairCreatedAt": 1698813068000
	}, {
		"chainId": "bsc",
		"dexId": "mdex",
		"url": "https://dexscreener.com/bsc/0x82e8f9e7624fa038dff4a39960f5197a43fa76aa",
		"pairAddress": "0x82E8F9e7624fA038DfF4a39960F5197A43fa76aa",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9594",
		"priceUsd": "3307.55",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 7
			},
			"h24": {
				"buys": 14,
				"sells": 18
			}
		},
		"volume": {
			"h24": 932.3,
			"h6": 157.04,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": -1.18,
			"h24": -6.81
		},
		"liquidity": {
			"usd": 71546.61,
			"base": 10.8156,
			"quote": 64.4557
		},
		"fdv": 2001020750
	}, {
		"chainId": "bsc",
		"dexId": "0x7897C32cbda1935e97c0B59F244747562D4d97c1",
		"url": "https://dexscreener.com/bsc/0xf7efddfcda24efd1c1a48dc9ceff6004a7c0f1bb",
		"pairAddress": "0xf7efDdFcda24EfD1c1a48DC9ceFf6004a7C0F1bb",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3293.6961",
		"priceUsd": "3293.69",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 1
			},
			"h6": {
				"buys": 3,
				"sells": 9
			},
			"h24": {
				"buys": 22,
				"sells": 33
			}
		},
		"volume": {
			"h24": 4940.36,
			"h6": 685.48,
			"h1": 84.72,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -0.51,
			"h6": -2.35,
			"h24": -7.09
		},
		"liquidity": {
			"usd": 65798.81,
			"base": 9.9885,
			"quote": 32899
		},
		"fdv": 1992635463,
		"pairCreatedAt": 1627635476000
	}, {
		"chainId": "bsc",
		"dexId": "0x3657952d7bA5A0A4799809b5B6fdfF9ec5B46293",
		"url": "https://dexscreener.com/bsc/0x8485c5f255ff30aafab0030329e508bd8dde11c5",
		"pairAddress": "0x8485c5f255FF30AafaB0030329e508BD8dDE11c5",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9610",
		"priceUsd": "3299.81",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 5
			},
			"h24": {
				"buys": 8,
				"sells": 13
			}
		},
		"volume": {
			"h24": 629.98,
			"h6": 125.41,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": -1.42,
			"h24": -7.1
		},
		"liquidity": {
			"usd": 58461.45,
			"base": 8.8582,
			"quote": 52.8048
		},
		"fdv": 1996338258
	}, {
		"chainId": "bsc",
		"dexId": "babyswap",
		"url": "https://dexscreener.com/bsc/0xfa0c1bd534784b978b4d5c426836f7c44f5c0b20",
		"pairAddress": "0xfa0C1bD534784b978b4d5c426836f7c44f5C0b20",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3292.6991",
		"priceUsd": "3292.69",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 1,
				"sells": 2
			},
			"h6": {
				"buys": 8,
				"sells": 13
			},
			"h24": {
				"buys": 39,
				"sells": 48
			}
		},
		"volume": {
			"h24": 3307.68,
			"h6": 895.81,
			"h1": 142.66,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": -0.48,
			"h6": -2.53,
			"h24": -7.71
		},
		"liquidity": {
			"usd": 51131.53,
			"base": 7.7643,
			"quote": 25565
		},
		"fdv": 1992032310,
		"pairCreatedAt": 1622556499000
	}, {
		"chainId": "bsc",
		"dexId": "squadswap",
		"url": "https://dexscreener.com/bsc/0x67e1362cf56b01fda35d4cfaafe08f0e28cda33b",
		"pairAddress": "0x67e1362cF56B01fDA35d4CfAaFE08F0e28cDA33b",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0x55d398326f99059fF775485246999027B3197955",
			"name": "Tether USD",
			"symbol": "USDT"
		},
		"priceNative": "3299.2876",
		"priceUsd": "3299.28",
		"txns": {
			"m5": {
				"buys": 1,
				"sells": 0
			},
			"h1": {
				"buys": 3,
				"sells": 3
			},
			"h6": {
				"buys": 6,
				"sells": 12
			},
			"h24": {
				"buys": 31,
				"sells": 32
			}
		},
		"volume": {
			"h24": 4117.55,
			"h6": 846.09,
			"h1": 277.55,
			"m5": 73.48
		},
		"priceChange": {
			"m5": 0.6,
			"h1": -0.29,
			"h6": -2.4,
			"h24": -7.08
		},
		"liquidity": {
			"usd": 49039.3,
			"base": 7.4318,
			"quote": 24519
		},
		"fdv": 1996018266,
		"pairCreatedAt": 1703923409000
	}, {
		"chainId": "bsc",
		"dexId": "bakeryswap",
		"url": "https://dexscreener.com/bsc/0xa50b9c5db61c855d5939aa1a66b26df77745809b",
		"pairAddress": "0xa50b9c5DB61C855D5939aa1a66B26Df77745809b",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9540",
		"priceUsd": "3304.79",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 3,
				"sells": 13
			},
			"h24": {
				"buys": 41,
				"sells": 26
			}
		},
		"volume": {
			"h24": 822.41,
			"h6": 132.01,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": -1.23,
			"h24": -7.37
		},
		"liquidity": {
			"usd": 46863.19,
			"base": 7.09018,
			"quote": 42.2153
		},
		"fdv": 1999349307
	}, {
		"chainId": "bsc",
		"dexId": "0x9Ad32bf5DaFe152Cbe027398219611DB4E8753B3",
		"url": "https://dexscreener.com/bsc/0x640e2c0eccd822f79951b6e63a44786c475e75b4",
		"pairAddress": "0x640E2c0EcCd822F79951b6E63A44786c475E75b4",
		"baseToken": {
			"address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
			"name": "Ethereum Token",
			"symbol": "ETH"
		},
		"quoteToken": {
			"address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
			"name": "Wrapped BNB",
			"symbol": "WBNB"
		},
		"priceNative": "5.9670",
		"priceUsd": "3320.38",
		"txns": {
			"m5": {
				"buys": 0,
				"sells": 0
			},
			"h1": {
				"buys": 0,
				"sells": 0
			},
			"h6": {
				"buys": 0,
				"sells": 2
			},
			"h24": {
				"buys": 3,
				"sells": 6
			}
		},
		"volume": {
			"h24": 351.37,
			"h6": 75.54,
			"h1": 0,
			"m5": 0
		},
		"priceChange": {
			"m5": 0,
			"h1": 0,
			"h6": -0.66,
			"h24": -6.4
		},
		"liquidity": {
			"usd": 38220.68,
			"base": 5.7554,
			"quote": 34.3431
		},
		"fdv": 2008781100
	}]
}

'''
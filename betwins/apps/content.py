"""Site-wide content for the casino website.

Everything that is "words" lives here (brand, contact details, games, tournaments,
blog posts, FAQs ...) so the templates stay layout-only.  Edit this file to change
the copy, phone numbers, addresses, etc. in one place.
"""

# ---------------------------------------------------------------------------
# Brand & contact details  (placeholders - replace with the real ones)
# ---------------------------------------------------------------------------
SITE = {
    "name": "Casino Royale",
    "short": "Casino Royale",
    "legal": "Casino Royale Entertainment Pvt. Ltd.",
    "tagline": "India's Luxury Casino & Resort",
    "about_short": (
        "Casino Royale is India's premier luxury casino & resort - a palace of "
        "world-class gaming, private salons, fine dining and legendary Indian hospitality."
    ),
    "phones": [
        {"label": "+91 832 255 0188", "href": "+918322550188", "note": "Reservations & Concierge"},
        {"label": "+91 98905 12345", "href": "+919890512345", "note": "WhatsApp VIP Desk"},
    ],
    "emails": [
        {"label": "concierge@casinoroyale.in", "note": "Concierge & Reservations"},
        {"label": "support@casinoroyale.in", "note": "Player Support"},
    ],
    "address": "Casino Royale Casino & Resort, Mandovi Riverfront, Dayanand Bandodkar Marg, Panaji, Goa 403001, India",
    "address_short": "Mandovi Riverfront, Panaji, Goa 403001",
    "map_link": "https://www.google.com/maps/search/?api=1&query=Mandovi+Riverfront+Panaji+Goa",
    "map_embed": "https://www.google.com/maps?q=Mandovi+Riverfront,+Panaji,+Goa&output=embed",
    "hours": "Gaming floor open 24 x 7  |  Support desk 24 x 7",
    "offices": [
        {"city": "Goa (Flagship)", "icon": "ti-building-skyscraper",
         "text": "Mandovi Riverfront, Dayanand Bandodkar Marg, Panaji, Goa 403001"},
        {"city": "Mumbai Royale Lounge", "icon": "ti-crown",
         "text": "Level 4, One BKC, G Block, Bandra Kurla Complex, Mumbai 400051"},
        {"city": "Delhi Royale Lounge", "icon": "ti-diamond",
         "text": "Hospitality District, Aerocity, New Delhi 110037"},
    ],
    "social": [
        {"icon": "fa-brands fa-facebook-f", "name": "facebook", "href": "https://www.facebook.com/"},
        {"icon": "fa-brands fa-instagram", "name": "instagram", "href": "https://instagram.com/"},
        {"icon": "fa-brands fa-x-twitter", "name": "x", "href": "https://x.com/"},
        {"icon": "fa-brands fa-youtube", "name": "youtube", "href": "https://www.youtube.com/"},
        {"icon": "fa-brands fa-whatsapp", "name": "whatsapp", "href": "https://wa.me/919890512345"},
    ],
    "min_age": 21,
}

# ---------------------------------------------------------------------------
# Navigation (flat - no dropdowns)
# ---------------------------------------------------------------------------
NAV = [
    {"label": "Home", "href": "/", "match": ["index"]},
    {"label": "About Us", "href": "/about-us", "match": ["about-us"]},
    {"label": "Games", "href": "/games", "match": ["games", "game-details", "lucky-draw"]},
    {"label": "Live Casino", "href": "/live-casino", "match": ["live-casino"]},
    {"label": "Tournaments", "href": "/tournaments", "match": ["tournaments", "tournament-details", "results", "jackpots"]},
    {"label": "VIP Club", "href": "/vip-club", "match": ["vip-club"]},
    {"label": "Blog", "href": "/blog", "match": ["blog", "blog-grid", "blog-details"]},
    {"label": "Contact", "href": "/contact-us", "match": ["contact-us"]},
]

PAYMENTS = ["upi", "phonepe", "paytm", "rupay", "netbanking", "imps"]  # casino/<name>.svg
PAYMENTS_RASTER = ["visa", "mastercard", "gpay"]                       # payment/<name>.png
SPONSORS = ["aurum", "nexa", "zenith", "sapphire", "vega", "orbit", "regal"]

# ---------------------------------------------------------------------------
# Games
# ---------------------------------------------------------------------------
def _g(slug, title, cats, kind, img, rating, ratings, rtp, bet_min, bet_max, playing, badge, tagline, intro, how, features, rules):
    return dict(slug=slug, title=title, cats=cats, kind=kind, img=img, rating=rating, ratings=ratings, rtp=rtp,
                bet_min=bet_min, bet_max=bet_max, playing=playing, badge=badge, tagline=tagline,
                intro=intro, how=how, features=features, rules=rules)


GAMES = [
    _g("teen-patti-royale", "Teen Patti Royale", ["indian", "live"], "Indian Cards", "casino/g-teen-patti.svg", "4.9", "12.4K",
       "97.8%", "₹500", "₹5,00,000", "1.2K", "Most Played",
       "India's favourite three-card showdown, dealt live by our Royale hostesses.",
       ["Teen Patti is the game that fills every Diwali evening across India - and at Casino Royale it gets the five-star treatment. Play against our live dealer on a private felt, with Boot, Pair Plus and Six-Card Bonus side bets running on every hand.",
        "Each round is streamed in ultra-HD from our Goa gaming floor, shuffled by certified card shufflers, and every hand is logged so you can review your history at any time."],
       ["Place your ante (and an optional Pair Plus side bet) before the cards are dealt.",
        "You and the dealer each receive three cards - you may play 'Blind' or look at your hand.",
        "Choose to Fold or Raise (Play) by matching your ante at least once.",
        "The best three-card hand wins: Trail (Set) > Pure Sequence > Sequence > Colour > Pair > High Card."],
       ["Ante, Pair Plus and Six-Card Bonus side bets", "Real-time hand history & statistics", "Private tables from ₹25,000 a seat", "Hindi, English and Marathi-speaking hosts"],
       ["The dealer qualifies with Queen-high or better; otherwise the ante is paid 1:1 and the raise is returned.",
        "Pair Plus pays 1:1 on a pair, 4:1 on a colour, 6:1 on a sequence, 35:1 on a pure sequence and 40:1 on a trail.",
        "Hand ties are settled as a push. All payouts are credited to your wallet instantly."]),
    _g("andar-bahar-classic", "Andar Bahar Classic", ["indian", "live"], "Indian Cards", "casino/g-andar-bahar.svg", "4.8", "9.8K",
       "97.9%", "₹200", "₹2,50,000", "980", "Fan Favourite",
       "The beloved desi card duel - pick Andar or Bahar and watch the joker decide.",
       ["Andar Bahar is one of the oldest and fastest card games in India. A single joker card is dealt face up, and you simply bet on whether the matching card will land on the Andar (inside) or Bahar (outside) side.",
        "Our live dealers deal at a brisk pace, so a round takes under a minute. Rounds are streamed from the Goa floor with multiple camera angles and a live chat host."],
       ["Watch the joker card being placed face up in the centre of the table.",
        "Bet on Andar or Bahar before the betting timer ends (20 seconds).",
        "Cards are dealt alternately to Andar and Bahar until a card of the joker's rank appears.",
        "The side that receives the matching card wins the round."],
       ["20-second rounds with clear on-screen timers", "Side bets on first-card colour and total cards dealt", "Live statistics of the last 100 rounds", "Mobile-optimised portrait view"],
       ["If the first card dealt matches the joker on Andar, Andar pays 0.9:1; any other Andar win pays 1:1.",
        "Bahar wins pay 1:1 (no commission). Side bets pay up to 25:1.",
        "A betting round is final once the timer expires; no bets can be modified after the cards are dealt."]),
    _g("dragon-tiger", "Dragon Tiger", ["indian", "table", "live"], "Fast Cards", "casino/g-dragon-tiger.svg", "4.7", "6.2K",
       "96.3%", "₹300", "₹3,00,000", "640", "Fast Action",
       "One card each for the Dragon and the Tiger - the highest card takes the pot.",
       ["Dragon Tiger distils baccarat down to a single decision: which of two hands will hold the higher card? With one card dealt to each side, this is the fastest game on our floor.",
        "It is also one of the most popular games with our high-roller guests - bet limits go up to ₹3,00,000 per round."],
       ["Place a bet on Dragon, Tiger, or the Tie before the round starts.",
        "One card is dealt to Dragon and one to Tiger.",
        "The higher card wins (Ace is low, King is high).",
        "On a Tie, half of your Dragon / Tiger stake is returned."],
       ["Suit bets and odd / even side bets", "Round times under 25 seconds", "Squeeze-style card reveals", "Live roadmap of results"],
       ["Dragon and Tiger pay 1:1. A Tie pays 8:1. Suited Tie pays 50:1.",
        "If the round ends in a Tie, Dragon and Tiger bets lose half their stake.",
        "The Ace is the lowest card; the King is the highest."]),
    _g("european-roulette", "European Roulette", ["table", "live"], "Roulette", "game/nineteen.png", "4.9", "15.1K",
       "97.3%", "₹100", "₹10,00,000", "1.8K", "Classic",
       "37 pockets, one ball and a single zero - the original, elegant roulette.",
       ["Our European Roulette wheel is hand-spun by a live croupier in Goa and broadcast in cinematic quality. With a single zero, it offers a house edge of just 2.7% - the best odds in the roulette family.",
        "From inside bets on a single number to outside bets on colours and dozens, you decide your own level of risk."],
       ["Choose your chip value and place bets on the table layout.",
        "The croupier spins the wheel and releases the ball against the rotation.",
        "Bets close just before the ball drops into a pocket.",
        "Winning bets are paid and the chips are cleared for the next spin."],
       ["Neighbour, Voisins du Zéro, Tiers and Orphelins call bets", "Favourite-number quick bets", "Multi-camera replays and slow-motion ball drop", "Auto-rebet and double-up controls"],
       ["Straight-up numbers pay 35:1, splits 17:1, streets 11:1, corners 8:1.",
        "Dozens and columns pay 2:1; red / black, odd / even and high / low pay 1:1.",
        "A 'la partage' rule returns half of even-money bets when the ball lands on zero."]),
    _g("royal-roulette-vip", "Royal Roulette VIP", ["table", "live"], "Roulette", "game/eighteen.png", "4.9", "7.7K",
       "97.3%", "₹5,000", "₹25,00,000", "310", "VIP Only",
       "A private roulette salon with higher limits and a dedicated croupier.",
       ["Royal Roulette VIP is reserved for Gold, Platinum and Maharaja members. The salon is hosted by a dedicated senior croupier, offers higher table limits and a quieter, more personal experience.",
        "Enjoy complimentary beverages when you play on our floor, or priority withdrawals when you play online."],
       ["Sign in with your VIP membership and choose a seat.",
        "Place your bets on the electronic layout or by calling bets to your host.",
        "The senior croupier spins the wheel for your table only.",
        "Winnings are credited instantly to your VIP wallet."],
       ["Private salon with seats limited to six guests", "Maximum bets up to ₹25,00,000", "Dedicated host on WhatsApp", "Priority payouts under 15 minutes"],
       ["Rules and payouts follow European Roulette with 'la partage'.",
        "A minimum Gold tier membership is required to join the salon.",
        "Seat reservations are held for 15 minutes."]),
    _g("blackjack-elite", "Blackjack Elite", ["table", "live"], "Blackjack", "casino/g-blackjack.svg", "4.8", "10.3K",
       "99.5%", "₹500", "₹5,00,000", "870", "Best Odds",
       "Beat the dealer to 21 - the casino game where strategy really pays.",
       ["Blackjack Elite uses a six-deck shoe and generous rules that give a house edge of under 0.5% when you follow basic strategy.",
        "Play at open tables with six other players, or reserve a private table for you and your friends."],
       ["Place your bet and receive two cards; the dealer shows one card.",
        "Hit to take another card, Stand to keep your total, Double Down or Split pairs.",
        "Get closer to 21 than the dealer without going over.",
        "Blackjack (Ace + 10-value card) pays 3:2."],
       ["Perfect Pairs and 21+3 side bets", "Insurance and Surrender options", "Bet Behind at full tables", "Basic strategy hints for beginners"],
       ["Blackjack pays 3:2. Insurance pays 2:1.",
        "The dealer must stand on all 17s and draw to 16.",
        "Double after split is allowed. Split aces receive one card each."]),
    _g("baccarat-prestige", "Baccarat Prestige", ["table", "live"], "Baccarat", "casino/g-baccarat.svg", "4.8", "8.9K",
       "98.9%", "₹1,000", "₹10,00,000", "720", "High Roller",
       "Punto Banco in its most refined form - Banker, Player or Tie.",
       ["Baccarat Prestige is played at a private oval table by a team of Royale dealers. The rules are simple: bet on Player, Banker or Tie and see which hand lands closest to nine.",
        "With the lowest house edge of any bet at the table (Banker 1.06%), this is a favourite with our high-roller guests."],
       ["Place your bet on Player, Banker or Tie.",
        "Two cards are dealt to the Player and Banker hands.",
        "A third card may be drawn according to fixed rules.",
        "The hand closest to a total of nine wins."],
       ["Squeeze mode for dramatic card reveals", "Player / Banker pair side bets", "Live scoreboards and road maps", "Commission-free (Super 6) tables"],
       ["Player pays 1:1. Banker pays 0.95:1 (5% commission). Tie pays 8:1.",
        "Player Pair and Banker Pair pay 11:1.",
        "Card values: 2-9 face value, 10/J/Q/K = 0, Ace = 1."]),
    _g("texas-holdem-poker", "Texas Hold'em Poker", ["table", "tournament"], "Poker", "casino/g-poker.svg", "4.7", "7.1K",
       "N/A (skill)", "₹1,000", "No limit", "560", "Skill Game",
       "No-limit Hold'em cash tables and tournaments with the sharpest players in India.",
       ["Our poker room runs cash games and daily tournaments with buy-ins from ₹1,000 to ₹1,00,000. Sit down at a table of six or nine and take on players from Mumbai to Chennai.",
        "The Casino Royale Poker Championship is the flagship event, with a guaranteed prize pool of ₹1 Crore."],
       ["Join a cash table or register for a tournament.",
        "Each player gets two private hole cards; five community cards follow.",
        "Bet, call, raise or fold over four rounds of betting.",
        "Make the best five-card hand to win the pot."],
       ["Daily freezeouts, turbo and deep-stack events", "Rakeback for VIP members", "Anonymous tables and tournament lobbies", "Live floor support from poker directors"],
       ["Standard Texas Hold'em rules apply with a 5% rake capped at ₹500 per hand (cash).",
        "Tournaments follow Tournament Directors Association (TDA) rules.",
        "Collusion or the use of poker bots leads to account closure."]),
    _g("sic-bo", "Sic Bo", ["table", "live"], "Dice", "casino/g-sic-bo.svg", "4.6", "4.2K",
       "97.2%", "₹200", "₹2,00,000", "410", "Dice Game",
       "Three dice, dozens of bets - the ancient game of chance, reimagined.",
       ["Sic Bo is a thrilling dice game of Chinese origin with some of the widest betting options on our floor. Predict the total, specific numbers or combinations after the dealer shakes three dice.",
        "Choose between low-risk 'Big / Small' bets or go all in on a Triple for payouts up to 180:1."],
       ["Place bets on the betting grid before the timer ends.",
        "The dealer shakes three dice in a sealed shaker.",
        "The dice are revealed and bets are settled.",
        "Winning bets are paid according to the payout table."],
       ["Slow-motion dice replays", "Lucky Number multiplier bets", "Hot / cold number statistics", "Quick-bet chips"],
       ["Big / Small pay 1:1 but lose on any triple.",
        "Single number bets pay 1:1, 2:1 or 3:1 depending on how many dice show the number.",
        "A specific triple pays 180:1; any triple pays 30:1."]),
    _g("royal-777-deluxe", "Royal 777 Deluxe", ["slot"], "Slots", "game/seventeen.png", "4.8", "13.6K",
       "96.5%", "₹10", "₹5,000", "2.4K", "Hot Slot",
       "Classic sevens, royal wilds and a free-spin feature that can pay up to 5,000x.",
       ["Royal 777 Deluxe brings the nostalgia of the classic fruit machine to a luxurious 5-reel layout with 25 paylines. Look out for the Maharaja Wild, which substitutes for all symbols and multiplies your win.",
        "Three or more golden Scatter symbols trigger up to 20 free spins with sticky wilds."],
       ["Select your bet per line and the number of lines (up to 25).",
        "Press Spin or enable Autoplay for up to 100 spins.",
        "Land matching symbols on a payline from left to right.",
        "Trigger the Free Spins feature with three or more Scatters."],
       ["96.5% theoretical RTP", "Medium-high volatility", "Free spins with sticky Maharaja Wilds", "Gamble feature (optional)"],
       ["Wins are calculated by multiplying the line bet by the payout.",
        "Malfunction voids all pays and plays.",
        "Maximum win is capped at 5,000x the total bet."]),
    _g("maharaja-megaways", "Maharaja Megaways", ["slot"], "Slots", "game/fourteen.png", "4.9", "11.2K",
       "96.2%", "₹20", "₹10,000", "1.9K", "New",
       "Up to 117,649 ways to win with cascading reels and a growing multiplier.",
       ["Maharaja Megaways takes you through a palace of riches with six reels and a different number of symbols on every spin. Winning symbols explode and are replaced, creating cascades that can chain into big wins.",
        "During free spins, the multiplier increases with every cascade - and never resets."],
       ["Choose your total bet and spin the reels.",
        "Match symbols on adjacent reels from left to right.",
        "Winning symbols are removed and new ones fall into place.",
        "Land four Scatters to unlock free spins with an unlimited multiplier."],
       ["Up to 117,649 ways to win", "Cascading wins and progressive multipliers", "Buy Feature option", "High volatility with 50,000x max win"],
       ["Ways pay left to right on adjacent reels.",
        "The Buy Feature costs 100x the current bet.",
        "Maximum win is capped at 50,000x."]),
    _g("golden-fortune", "Golden Fortune", ["slot", "jackpot"], "Slots", "game/twelve.png", "4.7", "5.8K",
       "96.0%", "₹10", "₹2,500", "1.1K", "Jackpot Slot",
       "Four progressive jackpots hide behind a single golden wheel.",
       ["Golden Fortune is a lavish 5x3 slot with a twist: any spin can trigger the Fortune Wheel, which awards one of four progressive jackpots - Bronze, Silver, Gold or Maharaja.",
        "The Maharaja jackpot has paid out over ₹3 Crore to a lucky player from Pune."],
       ["Pick your stake and spin.",
        "Land the golden coin symbol to fill the Fortune Meter.",
        "When the meter is full, the Fortune Wheel appears.",
        "Spin the wheel to win one of four jackpots."],
       ["Four progressive jackpots", "Fortune Meter bonus", "Expanding wilds", "Mobile-first design"],
       ["Jackpot winners are verified and announced within 24 hours.",
        "All jackpot wins above ₹10,000 are subject to TDS as per applicable Indian tax rules.",
        "Minimum stake for jackpot eligibility is ₹20."]),
    _g("casino-royale-jackpot-wheel", "Casino Royale Jackpot Wheel", ["jackpot"], "Jackpot", "game/sixteen.png", "4.9", "9.4K",
       "95.0%", "₹100", "₹50,000", "1.4K", "Mega Jackpot",
       "Spin the golden wheel for a shot at the Mega Jackpot, now over ₹12 Crore.",
       ["The Casino Royale Jackpot Wheel is the centrepiece of our floor. Every ₹100 bet contributes to a progressive jackpot that grows until it is won - and then resets to ₹1 Crore.",
        "Beyond the headline Mega Jackpot, there are Mini, Major and Grand prizes up for grabs on every spin."],
       ["Buy a spin (minimum ₹100) at any wheel station or on your member account.",
        "Spin the wheel and watch it slow down on a segment.",
        "Land on a jackpot segment to win the listed prize.",
        "Non-winning spins can earn bonus credits."],
       ["Network progressive jackpot across all floors", "Mini, Major, Grand and Mega prizes", "Live jackpot ticker on every screen", "Winner's ceremony and photo opportunity"],
       ["The Mega Jackpot is won by landing on the Mega segment at random.",
        "The jackpot is paid in full, in INR, via bank transfer after KYC verification.",
        "Winnings are subject to applicable taxes."]),
    _g("diwali-dhamaka-jackpot", "Diwali Dhamaka Jackpot", ["jackpot", "slot"], "Jackpot", "game/thirteen.png", "4.8", "6.5K",
       "95.8%", "₹50", "₹25,000", "860", "Festive Special",
       "A festival of lights, a festival of fortune - jackpot rounds every hour.",
       ["Diwali Dhamaka is our seasonal jackpot game, themed on the Festival of Lights with fireworks, diyas and golden rangoli patterns. A jackpot bonus drops at least once every hour, making it one of the most generous games on the floor.",
        "During Diwali week, all jackpot prizes are doubled."],
       ["Choose your bet level from ₹50.",
        "Spin the five reels and collect Diya symbols.",
        "Collect nine Diyas to trigger the Jackpot Round.",
        "Pick lanterns to reveal your prize."],
       ["Hourly must-drop jackpots", "Double prizes during Diwali week", "Pick-and-win bonus round", "Festive sound track"],
       ["The must-drop jackpot is guaranteed to fall before the stated amount.",
        "Prizes are paid in INR; promotional prize doubling applies during the festival period only.",
        "Players must be 21+ and KYC verified."]),
    _g("royal-keno", "Royal Keno", ["table", "lucky"], "Lucky Draw", "casino/g-keno.svg", "4.6", "3.9K",
       "95.5%", "₹50", "₹50,000", "520", "Lucky Draw",
       "Pick your lucky numbers and watch the draw - a game of pure fortune.",
       ["Royal Keno is our lottery-style game of chance. Choose up to five lucky numbers and a Joker number, then watch twenty numbers drawn live.",
        "Draws run every five minutes, so you are never more than a short wait from your next chance to win."],
       ["Choose five numbers from 1 to 40 and one Joker number from 1 to 30.",
        "Set your stake and confirm your ticket.",
        "Watch the draw balls roll out in the live draw.",
        "Match numbers to win - five matches plus the Joker wins the top prize."],
       ["Quick-pick for instant tickets", "Multi-draw tickets (up to 10 draws)", "Free number combinations", "Full draw history"],
       ["Top prize is 1,000x your stake.",
        "Prizes for matching two or more numbers are paid per the pay table.",
        "Tickets are final once purchased."]),
]

GAME_FILTERS = [
    {"key": "*", "label": "All Games", "icon": "ti-layout-grid"},
    {"key": ".slot", "label": "Slots", "icon": "ti-diamond"},
    {"key": ".table", "label": "Table Games", "icon": "ti-poker-chip"},
    {"key": ".indian", "label": "Indian Cards", "icon": "ti-cards"},
    {"key": ".jackpot", "label": "Jackpots", "icon": "ti-crown"},
]

# ---------------------------------------------------------------------------
# Live casino tables (live-casino page)
# ---------------------------------------------------------------------------
LIVE_TABLES = [
    {"title": "Teen Patti Royale", "slug": "teen-patti-royale", "img": "casino/t-teen-patti.svg", "cat": "indian", "label": "Indian Cards", "rating": "4.9", "limit": "₹500 - ₹5L", "seats": "5/7 seats"},
    {"title": "Andar Bahar Classic", "slug": "andar-bahar-classic", "img": "casino/t-andar-bahar.svg", "cat": "indian", "label": "Indian Cards", "rating": "4.8", "limit": "₹200 - ₹2.5L", "seats": "Open table"},
    {"title": "Dragon Tiger", "slug": "dragon-tiger", "img": "casino/t-dragon-tiger.svg", "cat": "indian", "label": "Fast Cards", "rating": "4.7", "limit": "₹300 - ₹3L", "seats": "Open table"},
    {"title": "European Roulette", "slug": "european-roulette", "img": "casino/t-roulette.svg", "cat": "roulette", "label": "Roulette", "rating": "4.9", "limit": "₹100 - ₹10L", "seats": "Open table"},
    {"title": "Blackjack Elite", "slug": "blackjack-elite", "img": "casino/t-blackjack.svg", "cat": "cards", "label": "Blackjack", "rating": "4.8", "limit": "₹500 - ₹5L", "seats": "4/7 seats"},
    {"title": "Baccarat Prestige", "slug": "baccarat-prestige", "img": "casino/t-baccarat.svg", "cat": "cards", "label": "Baccarat", "rating": "4.8", "limit": "₹1K - ₹10L", "seats": "3/7 seats"},
    {"title": "Texas Hold'em", "slug": "texas-holdem-poker", "img": "casino/t-poker.svg", "cat": "cards", "label": "Poker", "rating": "4.7", "limit": "₹1K - No limit", "seats": "6-max"},
    {"title": "Sic Bo", "slug": "sic-bo", "img": "casino/t-sic-bo.svg", "cat": "dice", "label": "Dice", "rating": "4.6", "limit": "₹200 - ₹2L", "seats": "Open table"},
    {"title": "Royal Roulette VIP", "slug": "royal-roulette-vip", "img": "casino/t-roulette.svg", "cat": "roulette", "label": "VIP Salon", "rating": "4.9", "limit": "₹5K - ₹25L", "seats": "2/6 seats"},
    {"title": "Royal Keno", "slug": "royal-keno", "img": "casino/t-keno.svg", "cat": "dice", "label": "Lucky Draw", "rating": "4.6", "limit": "₹50 - ₹50K", "seats": "Draw every 5 min"},
    {"title": "Maharaja Megaways", "slug": "maharaja-megaways", "img": "casino/t-slots.svg", "cat": "slots", "label": "Slots", "rating": "4.9", "limit": "₹20 - ₹10K", "seats": "Instant play"},
    {"title": "Casino Royale Jackpot Wheel", "slug": "casino-royale-jackpot-wheel", "img": "casino/t-jackpot.svg", "cat": "slots", "label": "Jackpot", "rating": "4.9", "limit": "₹100 - ₹50K", "seats": "Instant play"},
]

LIVE_FILTERS = [
    {"key": "*", "label": "All Tables", "icon": "ti-layout-grid"},
    {"key": ".indian", "label": "Indian Cards", "icon": "ti-cards"},
    {"key": ".roulette", "label": "Roulette", "icon": "ti-circle-dot"},
    {"key": ".cards", "label": "Cards", "icon": "ti-spade"},
    {"key": ".dice", "label": "Dice & Lucky", "icon": "ti-dice-5"},
    {"key": ".slots", "label": "Slots & Jackpot", "icon": "ti-crown"},
]

# ---------------------------------------------------------------------------
# Tournaments
# ---------------------------------------------------------------------------
TOURNAMENTS = [
    {"slug": "casino-royale-poker-championship", "code": "RPC", "title": "Casino Royale Poker Championship", "cats": ["poker"],
     "img": "casino/g-poker.svg", "buyin": "₹55,000", "prize": "₹1,00,00,000", "seats": "128 seats left", "starts": "22 Days",
     "dates": "5 - 9 Nov 2026", "format": "No-Limit Hold'em · Freezeout", "venue": "Royale Poker Room, Goa",
     "intro": "India's most prestigious poker tournament returns to Goa with a guaranteed prize pool of ₹1 Crore. Over five days, the country's finest players battle for the Maharaja bracelet and a seat in the Asia Poker Series.",
     "schedule": [("Day 1A / 1B", "Starting flights - 20,000 chips, 40-minute levels"), ("Day 2", "Registration closes, play to the money bubble"), ("Day 3", "Final two tables"), ("Day 4", "Final table - live streamed from the Royale Theatre")],
     "prizes": [("1st", "₹32,00,000 + Maharaja bracelet"), ("2nd", "₹18,00,000"), ("3rd", "₹10,50,000"), ("4th - 9th", "₹3,00,000 - ₹7,00,000")],
     "rules": ["Open to guests aged 21+ with valid government photo ID.", "Late registration is open until the start of Level 8.", "TDA rules apply; tournament director's decision is final.", "Prize payouts are made after KYC and applicable TDS deductions."]},
    {"slug": "teen-patti-maharaja-cup", "code": "TMC", "title": "Teen Patti Maharaja Cup", "cats": ["teenpatti"],
     "img": "casino/g-teen-patti.svg", "buyin": "₹10,000", "prize": "₹25,00,000", "seats": "310 seats left", "starts": "9 Days",
     "dates": "22 - 25 Oct 2026", "format": "Knockout · Table of 7", "venue": "Royale Floor & Live Online",
     "intro": "The ultimate showdown for India's favourite card game. Win your table, climb the bracket and claim the Maharaja Cup - with a festive twist ahead of Diwali.",
     "schedule": [("Round 1", "Table elimination - top 2 advance"), ("Round 2", "Semi-final tables"), ("Final", "Head-to-head live on the main stage")],
     "prizes": [("Winner", "₹10,00,000 + Maharaja Cup"), ("Runner-up", "₹5,00,000"), ("3rd", "₹2,50,000"), ("4th - 10th", "₹50,000 each")],
     "rules": ["Hands are played with a fixed ante and unlimited raises.", "Players act within 20 seconds.", "A player who leaves the table forfeits their seat.", "Online and on-floor players play in separate brackets."]},
    {"slug": "diwali-slots-showdown", "code": "DSS", "title": "Diwali Slots Showdown", "cats": ["slots"],
     "img": "game/seventeen.png", "buyin": "₹2,500", "prize": "₹15,00,000", "seats": "1,200 seats left", "starts": "26 Days",
     "dates": "8 - 12 Nov 2026", "format": "Leaderboard · 5 Days", "venue": "Online & Slot Floor",
     "intro": "Spin your way up the leaderboard during the Festival of Lights. Every spin earns points - the top 100 players share a mega prize pool in cash and festive gold coins.",
     "schedule": [("Day 1 - 4", "Qualifying spins on selected slots"), ("Day 5", "Leaderboard freezes at midnight"), ("Awards", "Winners announced on Bhai Dooj")],
     "prizes": [("1st", "₹5,00,000 + 10g gold coin"), ("2nd", "₹2,50,000"), ("3rd", "₹1,25,000"), ("4th - 100th", "Share of ₹6,25,000")],
     "rules": ["Points are earned per ₹ wagered on eligible slots.", "Bonus funds do not count toward leaderboard points.", "Cash prizes are credited within 48 hours.", "Gold coin prizes are collected from the Goa resort or delivered insured to your address."]},
    {"slug": "roulette-royale-open", "code": "RRO", "title": "Roulette Royale Open", "cats": ["roulette"],
     "img": "game/nineteen.png", "buyin": "₹5,000", "prize": "₹20,00,000", "seats": "240 seats left", "starts": "15 Days",
     "dates": "29 Oct - 1 Nov 2026", "format": "Points Race · 150 Spins", "venue": "Royale Roulette Salon",
     "intro": "Each player starts with the same virtual stack of 10,000 chips across 150 spins. The player who ends with the biggest stack wins - strategy and nerve decide the champion.",
     "schedule": [("Session 1", "50 spins - bet freely"), ("Session 2", "50 spins - minimum bet rises"), ("Final", "50 spins - top 20 only")],
     "prizes": [("1st", "₹8,00,000"), ("2nd", "₹4,00,000"), ("3rd", "₹2,00,000"), ("4th - 20th", "₹35,000 each")],
     "rules": ["All sessions use European Roulette with a single zero.", "Chips have no cash value.", "A player must wager at least 20 chips per spin.", "Ties are broken by highest single win."]},
    {"slug": "blackjack-blitz", "code": "BJB", "title": "Blackjack Blitz", "cats": ["blackjack"],
     "img": "casino/g-blackjack.svg", "buyin": "₹7,500", "prize": "₹12,00,000", "seats": "96 seats left", "starts": "12 Days",
     "dates": "26 - 28 Oct 2026", "format": "Shootout · 3 Rounds", "venue": "Royale Blackjack Pit",
     "intro": "A fast-paced shootout for strategy lovers. Every table is a mini-tournament - finish with the biggest stack after 30 hands to advance.",
     "schedule": [("Round 1", "30 hands - top 2 per table"), ("Round 2", "30 hands - top 2 per table"), ("Final", "50 hands - winner takes the Blitz trophy")],
     "prizes": [("Winner", "₹5,00,000"), ("Runner-up", "₹2,50,000"), ("3rd", "₹1,25,000"), ("4th - 6th", "₹50,000 each")],
     "rules": ["Six-deck shoe, dealer stands on soft 17.", "Surrender is not allowed in tournament play.", "Players must act within 15 seconds.", "Hands per round are fixed - no late additions."]},
    {"slug": "baccarat-high-rollers", "code": "BHR", "title": "Baccarat High Rollers Invitational", "cats": ["blackjack", "poker"],
     "img": "casino/g-baccarat.svg", "buyin": "₹1,00,000", "prize": "₹50,00,000", "seats": "24 seats left", "starts": "35 Days",
     "dates": "16 - 18 Nov 2026", "format": "Invitational · Private Salon", "venue": "Maharaja Salon, Goa",
     "intro": "An invitation-only event for Platinum and Maharaja members. Three days of baccarat in the Maharaja Salon, with private dining, luxury hospitality and a ₹50 Lakh prize pool.",
     "schedule": [("Day 1", "Welcome dinner and seeded round"), ("Day 2", "Semi-finals"), ("Day 3", "Final and gala award night")],
     "prizes": [("Winner", "₹20,00,000 + luxury watch"), ("Runner-up", "₹10,00,000"), ("3rd", "₹5,00,000")],
     "rules": ["Open to Platinum and Maharaja members by invitation.", "Complimentary two-night stay included.", "Dress code: black tie / traditional formal.", "Prizes are subject to KYC and applicable taxes."]},
]

TOURNAMENT_FILTERS = [
    {"key": "*", "label": "All Events", "icon": "ti-layout-grid"},
    {"key": ".poker", "label": "Poker", "icon": "ti-spade"},
    {"key": ".teenpatti", "label": "Teen Patti", "icon": "ti-cards"},
    {"key": ".slots", "label": "Slots", "icon": "ti-diamond"},
    {"key": ".roulette", "label": "Roulette", "icon": "ti-circle-dot"},
    {"key": ".blackjack", "label": "Blackjack", "icon": "ti-dice-5"},
]

# ---------------------------------------------------------------------------
# Jackpots & draw results
# ---------------------------------------------------------------------------
JACKPOTS = [
    {"title": "Casino Royale Mega Jackpot", "amount": "₹12.4 Cr", "img": "casino/t-jackpot.svg", "game": "casino-royale-jackpot-wheel"},
    {"title": "Maharaja Grand", "amount": "₹4.85 Cr", "img": "casino/t-slots.svg", "game": "maharaja-megaways"},
    {"title": "Diwali Dhamaka", "amount": "₹2.1 Cr", "img": "casino/t-keno.svg", "game": "diwali-dhamaka-jackpot"},
    {"title": "Golden Fortune Major", "amount": "₹92 L", "img": "casino/t-slots.svg", "game": "golden-fortune"},
    {"title": "Royal Keno Top Prize", "amount": "₹50 L", "img": "casino/t-keno.svg", "game": "royal-keno"},
    {"title": "Teen Patti Bonus Pot", "amount": "₹38 L", "img": "casino/t-teen-patti.svg", "game": "teen-patti-royale"},
    {"title": "Roulette Lucky Spin", "amount": "₹24 L", "img": "casino/t-roulette.svg", "game": "european-roulette"},
    {"title": "Baccarat Bonus Pot", "amount": "₹18 L", "img": "casino/t-baccarat.svg", "game": "baccarat-prestige"},
]

RESULTS = [
    {"no": "KN-48213", "title": "Royal Keno - Evening Draw", "img": "game/fifteen.png", "date": "12/10/2026", "ago": "27m ago", "numbers": [7, 14, 21, 33, 38]},
    {"no": "DD-30977", "title": "Diwali Dhamaka Draw", "img": "game/thirteen.png", "date": "12/10/2026", "ago": "2h ago", "numbers": [3, 9, 17, 25, 36]},
    {"no": "KN-48190", "title": "Royal Keno - Afternoon Draw", "img": "game/eleven.png", "date": "12/10/2026", "ago": "5h ago", "numbers": [2, 11, 19, 28, 40]},
    {"no": "RM-10412", "title": "Casino Royale Mega Draw", "img": "game/sixteen.png", "date": "11/10/2026", "ago": "1d ago", "numbers": [5, 12, 23, 31, 37]},
    {"no": "KN-48044", "title": "Royal Keno - Late Night Draw", "img": "game/fourteen.png", "date": "11/10/2026", "ago": "1d ago", "numbers": [1, 8, 16, 24, 35]},
    {"no": "GF-22871", "title": "Golden Fortune Draw", "img": "game/seventeen.png", "date": "10/10/2026", "ago": "2d ago", "numbers": [4, 10, 18, 27, 39]},
]

# ---------------------------------------------------------------------------
# Winners (illustrative) - avatars are from /static/images/avatar
# ---------------------------------------------------------------------------
WINNERS = [
    {"name": "Arjun Mehta", "city": "Mumbai", "game": "Teen Patti", "bet": "₹25,000", "win": "₹4,12,500", "av": "one"},
    {"name": "Priya Nair", "city": "Kochi", "game": "Roulette", "bet": "₹10,000", "win": "₹3,50,000", "av": "two"},
    {"name": "Rohan Deshmukh", "city": "Pune", "game": "Jackpot", "bet": "₹500", "win": "₹3,18,00,000", "av": "three"},
    {"name": "Aarav Sharma", "city": "New Delhi", "game": "Poker", "bet": "₹55,000", "win": "₹9,80,000", "av": "four"},
    {"name": "Meera Iyer", "city": "Chennai", "game": "Baccarat", "bet": "₹50,000", "win": "₹2,45,000", "av": "five"},
    {"name": "Vikram Singh", "city": "Jaipur", "game": "Slots", "bet": "₹200", "win": "₹1,82,000", "av": "six"},
    {"name": "Ananya Reddy", "city": "Hyderabad", "game": "Blackjack", "bet": "₹15,000", "win": "₹1,12,500", "av": "seven"},
    {"name": "Kabir Khanna", "city": "Chandigarh", "game": "Andar Bahar", "bet": "₹8,000", "win": "₹96,000", "av": "eight"},
]

CHAMPIONS = [
    ("Arjun Mehta", "a-one", "Won 45 minutes ago", "Mumbai"),
    ("Priya Nair", "a-two", "Won 2 hours ago", "Kochi"),
    ("Rohan Deshmukh", "a-three", "Won 3 hours ago", "Pune"),
    ("Aarav Sharma", "a-four", "Won 5 hours ago", "New Delhi"),
    ("Meera Iyer", "a-five", "Won 6 hours ago", "Chennai"),
    ("Vikram Singh", "a-six", "Won yesterday", "Jaipur"),
    ("Ananya Reddy", "a-seven", "Won yesterday", "Hyderabad"),
    ("Kabir Khanna", "a-eight", "Won 2 days ago", "Chandigarh"),
]

# winners table (live casino page): rows per tab
WIN_ROWS = {
    "slots": [("Vikram Singh", "one", "Royal 777 Deluxe", "₹200", "₹1,82,000"), ("Siddharth Rao", "nine", "Maharaja Megaways", "₹500", "₹1,45,000"),
              ("Neha Kapoor", "ten", "Golden Fortune", "₹100", "₹82,500"), ("Ishaan Gupta", "eleven", "Royal 777 Deluxe", "₹250", "₹64,000"),
              ("Farhan Qureshi", "twelve", "Maharaja Megaways", "₹300", "₹51,300")],
    "cards": [("Arjun Mehta", "two", "Teen Patti", "₹25,000", "₹4,12,500"), ("Aarav Sharma", "three", "Poker", "₹55,000", "₹9,80,000"),
              ("Ananya Reddy", "four", "Blackjack", "₹15,000", "₹1,12,500"), ("Kabir Khanna", "five", "Andar Bahar", "₹8,000", "₹96,000"),
              ("Meera Iyer", "six", "Baccarat", "₹50,000", "₹2,45,000")],
    "roulette": [("Priya Nair", "seven", "European Roulette", "₹10,000", "₹3,50,000"), ("Rahul Verma", "eight", "Royal Roulette VIP", "₹40,000", "₹2,80,000"),
                 ("Tanvi Joshi", "nine", "European Roulette", "₹5,000", "₹1,75,000"), ("Dev Malhotra", "ten", "Royal Roulette VIP", "₹25,000", "₹1,25,000"),
                 ("Sneha Pillai", "eleven", "European Roulette", "₹2,000", "₹70,000")],
    "jackpot": [("Rohan Deshmukh", "twelve", "Casino Royale Jackpot Wheel", "₹500", "₹3,18,00,000"), ("Kavya Menon", "one", "Diwali Dhamaka", "₹50", "₹24,00,000"),
                ("Nikhil Bansal", "two", "Golden Fortune", "₹100", "₹8,40,000"), ("Zoya Ahmed", "three", "Casino Royale Jackpot Wheel", "₹100", "₹6,10,000"),
                ("Harsh Patel", "four", "Diwali Dhamaka", "₹50", "₹4,95,000")],
}

# ---------------------------------------------------------------------------
# Testimonials
# ---------------------------------------------------------------------------
TESTIMONIALS = [
    {"quote": "The most elegant casino I have ever played in. The Maharaja Salon is spectacular, the dealers are impeccable and my UPI withdrawal landed in under ten minutes.", "name": "Arjun Mehta", "role": "Entrepreneur, Mumbai", "av": "five", "date": "September 21, 2026", "handle": "@arjunm"},
    {"quote": "I came for a weekend in Goa and stayed for the Teen Patti tables. Fair, fast and beautifully run - Casino Royale feels like a true palace of luxury.", "name": "Priya Nair", "role": "Architect, Kochi", "av": "two", "date": "August 30, 2026", "handle": "@priyanair"},
    {"quote": "Their responsible gaming tools are the best I have seen - deposit limits, cool-off and a genuinely helpful support team available all night.", "name": "Rohan Deshmukh", "role": "Chartered Accountant, Pune", "av": "six", "date": "October 2, 2026", "handle": "@rohand"},
    {"quote": "The Poker Championship was run to international standards. Superb floor staff, great structure and the final table in the Royale Theatre was unforgettable.", "name": "Aarav Sharma", "role": "Poker Player, New Delhi", "av": "seven", "date": "September 11, 2026", "handle": "@aarav_s"},
    {"quote": "Live Roulette in HD with Hindi-speaking croupiers - it is a very different experience from other platforms. And I love the festival jackpots.", "name": "Meera Iyer", "role": "Doctor, Chennai", "av": "eight", "date": "July 18, 2026", "handle": "@meerai"},
    {"quote": "As a VIP member the concierge handles everything - flights, suites, table reservations. It is the definition of luxury hospitality in India.", "name": "Vikram Singh", "role": "Hotelier, Jaipur", "av": "nine", "date": "October 5, 2026", "handle": "@vikramsingh"},
    {"quote": "KYC took ten minutes, the interface is smooth on my phone and customer support actually replies on WhatsApp. Highly recommended.", "name": "Ananya Reddy", "role": "Product Manager, Hyderabad", "av": "four", "date": "August 9, 2026", "handle": "@ananyar"},
    {"quote": "I have played Blackjack Elite for months. The odds are fair and the rules are clearly explained - exactly what I expect from a premium casino.", "name": "Kabir Khanna", "role": "Investment Banker, Chandigarh", "av": "thirteen", "date": "September 28, 2026", "handle": "@kabirk"},
]

# ---------------------------------------------------------------------------
# Counters (about page / home)
# ---------------------------------------------------------------------------
COUNTERS = [
    {"icon": "ti-currency-rupee", "value": 850, "suffix": "Cr+", "label": "Total Winnings Paid Out"},
    {"icon": "ti-users", "value": 350, "suffix": "K+", "label": "Happy Guests & Players"},
    {"icon": "ti-device-gamepad-2", "value": 120, "suffix": "+", "label": "Premium Games & Tables"},
    {"icon": "ti-trophy", "value": 45, "suffix": "+", "label": "Tournaments Every Year"},
]

# ---------------------------------------------------------------------------
# VIP tiers
# ---------------------------------------------------------------------------
VIP_TIERS = [
    {"name": "Silver", "icon": "ti-diamond", "points": "0 - 24,999 pts", "perks": ["Welcome bonus up to ₹10,000", "Weekly cashback of 2%", "Access to member tournaments", "24x7 live chat support"]},
    {"name": "Gold", "icon": "ti-award", "points": "25,000 - 99,999 pts", "perks": ["Monthly cashback of 5%", "Royal Roulette VIP salon access", "Priority withdrawals under 1 hour", "Birthday gift and 2 complimentary dining vouchers"]},
    {"name": "Platinum", "icon": "ti-crown", "points": "1,00,000 - 4,99,999 pts", "perks": ["Dedicated host on WhatsApp", "Complimentary suite nights in Goa", "Invitations to the High Rollers Invitational", "Airport transfers and lounge access"]},
    {"name": "Maharaja", "icon": "ti-chess-king", "points": "5,00,000+ pts (invitation)", "perks": ["Private Maharaja Salon", "Personal concierge & jet transfers", "Custom-limit tables and bespoke events", "Annual Royale experience for two"]},
]

VIP_BENEFITS = [
    {"icon": "ti-gift", "title": "Welcome & Festival Gifts", "text": "Receive exclusive hampers, gold coins and surprise gifts at Diwali, Holi, Eid and New Year."},
    {"icon": "ti-bed", "title": "Suites & Spa Retreats", "text": "Enjoy complimentary stays in our riverfront suites, access to the Royale spa and chef's table dinners."},
    {"icon": "ti-plane", "title": "Concierge & Travel", "text": "Your personal host arranges flights, chauffeured airport pick-ups and reservations in 20+ Indian cities."},
    {"icon": "ti-cash", "title": "Cashback & Rakeback", "text": "Earn up to 10% weekly cashback and rakeback on poker, tracked automatically in your member dashboard."},
]

# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------
def _p(slug, title, cat, date, img, wide, thumb, comments, excerpt, sections):
    return dict(slug=slug, title=title, cat=cat, date=date, img=img, wide=wide, thumb=thumb, comments=comments,
                excerpt=excerpt, sections=sections)


POSTS = [
    _p("teen-patti-strategy-guide", "Teen Patti Strategy: When to Play Blind, Pack or Show", "Strategy", "12 Oct, 2026",
       "blog/six.png", "blog/ten.png", "blog/ph-one.png", 24,
       "Learn the odds behind every decision in India's favourite card game - from blind play to a perfectly timed show.",
       [("The Odds Behind the Cards", ["Teen Patti is played with a standard 52-card deck, giving 22,100 possible three-card hands. The chance of being dealt a trail (three of a kind) is just 0.24%, while a pair appears about 16.9% of the time. Knowing this, you can judge the strength of your hand before you place a bet.", "High card hands - those with no pair, sequence or colour - make up nearly 74% of all deals. That is why bluffing is such a central part of the game."]),
        ("Playing Blind vs. Playing Seen", ["Blind players only need to put in half the stake that seen players must match. This gives blind players a cost advantage but you give up information. A common rule of thumb is to stay blind until the pot reaches 8x the boot, then take a look.", "Seen players should pack (fold) any hand below a Queen-high without a pair, unless the table is very tight."]),
        ("Knowing When to Show", ["When only two players remain, either can ask for a show. If you hold a pair of eights or better, requesting a show is often the best option - particularly against an aggressive opponent who has been raising blind.", "Avoid showing with a low pair against a player who has been calling at every step; they are most likely holding a stronger hand."]),
        ("Bankroll Tips", ["Never play with more than 5% of your session bankroll in a single hand. Teen Patti is a high-variance game, and even the best strategy loses to a lucky trail from time to time.", "Set a time limit and a loss limit before you sit down - and stick to both."])]),
    _p("european-roulette-bets-explained", "The Royal Guide to European Roulette Bets", "Guides", "08 Oct, 2026",
       "casino/b-roulette-sq.svg", "casino/b-roulette-wide.svg", "blog/ph-two.png", 18,
       "From straight-up numbers to neighbour bets - a clear guide to every wager on the roulette layout.",
       [("Inside Bets", ["Inside bets are placed on the numbers themselves. A straight-up bet on a single number pays 35:1; split bets (two numbers) pay 17:1; street bets (three) pay 11:1; corners (four) pay 8:1; and six-line bets pay 5:1.", "These bets have lower odds of winning but higher payouts."]),
        ("Outside Bets", ["Outside bets cover large groups of numbers. Red or black, odd or even and high or low (1-18 / 19-36) pay 1:1 and win roughly 48.6% of the time. Dozens and columns pay 2:1.", "Outside bets are ideal for players who want longer sessions at the table."]),
        ("Call Bets and Neighbours", ["Our croupiers will place call bets for you - such as Voisins du Zéro (17 numbers around the zero), Tiers du Cylindre (12 numbers) and Orphelins (8 numbers). Neighbour bets cover a chosen number plus the two adjacent pockets on the wheel on either side.", "Remember: every bet carries the same 2.7% house edge, so the best 'system' is a budget."])]),
    _p("responsible-gaming-set-limits", "Responsible Play: How to Set Limits Like a Pro", "Responsible Gaming", "03 Oct, 2026",
       "blog/three.png", "blog/eleven.png", "blog/ph-three.png", 31,
       "A practical, no-judgement guide to deposit limits, time limits and cool-off periods.",
       [("Decide Before You Play", ["The most important limit is the one you set before the first bet. Decide how much you can comfortably afford to lose - treat it as the cost of an evening's entertainment, just like a movie ticket or dinner.", "Never gamble with money earmarked for rent, EMIs, school fees or savings."]),
        ("Use Our Built-in Tools", ["Casino Royale members can set daily, weekly or monthly deposit limits, loss limits, session time reminders and wager limits from their account. Limits can be lowered immediately; increases take effect after a 72-hour cooling-off period.", "You can also take a break from 24 hours to 6 months, or self-exclude for 1 to 5 years."]),
        ("Know the Warning Signs", ["Chasing losses, borrowing to gamble, lying about how much you play, or feeling anxious when you are not playing are all signs that it may be time to step back.", "Talk to our support team 24x7, or call the national helpline Tele-MANAS on 14416 for free, confidential support."])]),
    _p("inside-the-vip-salon", "Inside the Maharaja Salon: India's Most Exclusive Gaming Room", "VIP", "28 Sep, 2026",
       "blog/seven.png", "blog/ten.png", "blog/ph-four.png", 12,
       "Step behind the velvet ropes for a look at the private salon where Platinum and Maharaja members play.",
       [("A Palace within a Palace", ["The Maharaja Salon spans 6,000 square feet on the top floor of Casino Royale, with panoramic views over the Mandovi river. Hand-carved teak panels, Jaipur block-print silk and Murano chandeliers set the tone for an evening that feels more like a royal durbar than a casino.", "The salon seats a maximum of 40 guests at a time."]),
        ("Games & Limits", ["The salon offers private tables for Baccarat, Teen Patti, Roulette and Poker with table limits that start at ₹10,000 and can be customised for each guest.", "A dedicated host looks after every table, along with a sommelier and a chef de cuisine."]),
        ("How to Join", ["Platinum membership begins at 1,00,000 loyalty points. Maharaja membership is by invitation only. Speak to our concierge on WhatsApp to learn how to qualify.", "Smart-formal attire is requested; traditional Indian formals are most welcome."])]),
    _p("blackjack-basic-strategy", "Blackjack Basic Strategy: A Simple Chart You Can Memorise", "Strategy", "21 Sep, 2026",
       "casino/b-blackjack-sq.svg", "casino/b-blackjack-wide.svg", "blog/ph-one.png", 15,
       "Reduce the house edge to under 0.5% by learning when to hit, stand, double and split.",
       [("Why Basic Strategy Works", ["Basic strategy is a mathematically derived set of rules that tells you the best play for every combination of your hand and the dealer's up-card. It was calculated by computer simulations of millions of hands.", "Following it reduces the house edge on Blackjack Elite to under 0.5% - the lowest in the casino."]),
        ("The Golden Rules", ["Always stand on hard 17 or higher. Always hit hard 8 or lower. Always split aces and eights. Never split tens or fives. Double on 11 against any dealer card except an Ace.", "Never take insurance - it is a side bet with a high house edge."]),
        ("Soft Hands and Pairs", ["Soft hands contain an ace counted as 11. Hit soft 17 or lower; stand on soft 19 or higher; double soft 16-18 against a dealer 4, 5 or 6.", "Pairs are split depending on the dealer card - pairs of 2s, 3s and 7s are split against a dealer 2 through 7."])]),
    _p("diwali-festival-tournaments", "Diwali at Casino Royale: Tournaments, Gifts & Jackpots", "Events", "15 Sep, 2026",
       "blog/five.png", "blog/eleven.png", "blog/ph-two.png", 40,
       "Light a diya, join a tournament and share in ₹2 Crore of festive prizes this Diwali season.",
       [("A Festival of Fortune", ["Diwali is the traditional season for cards, and nowhere is it celebrated like at Casino Royale. From 22 October to 12 November, the resort is lit with thousands of diyas and a series of special events.", "Highlights include the Teen Patti Maharaja Cup, the Diwali Slots Showdown and double-prize jackpots."]),
        ("Gifts for Every Guest", ["Every member who plays during Diwali week receives a hand-crafted mithai box, and Gold and above members receive a silver coin. Platinum members are invited to a private Lakshmi Puja at the resort.", "Our chefs will serve a special Diwali buffet with 40 dishes from across India."]),
        ("Plan Your Visit", ["Resort suites are in high demand - book early. Our concierge can arrange flights, airport transfers and a themed Diwali package that includes dining, spa and tournament entries."])]),
    _p("baccarat-101", "Baccarat 101: Banker, Player or Tie?", "Guides", "09 Sep, 2026",
       "casino/b-baccarat-sq.svg", "casino/b-baccarat-wide.svg", "blog/ph-three.png", 9,
       "Why the Banker bet is the smartest wager at the table - and how the third-card rules work.",
       [("The Basics", ["In Baccarat, your goal is to bet on which hand - Player or Banker - will be closest to nine. Cards two to nine are worth face value, tens and face cards are zero and aces are one. If the total goes into double digits, only the last digit counts.", "The game is dealt entirely by the croupier, with no decisions required from the player."]),
        ("Which Bet is Best?", ["Banker has a house edge of 1.06% after the 5% commission, Player has 1.24% and Tie has a hefty 14.4%. The mathematical choice is clear: Banker, then Player, and avoid Tie.", "Pair side bets are fun but carry a larger house edge."]),
        ("Third Card Rules", ["If either hand totals 8 or 9, both stand (a 'natural'). Otherwise, the Player draws on 0-5 and stands on 6-7. The Banker's decision depends on the Player's third card and the Banker's own total.", "You do not need to memorise these - the dealer applies them automatically."])]),
    _p("provably-fair-rng-explained", "How Certified RNG and Live Dealers Keep Games Fair", "Fair Play", "02 Sep, 2026",
       "blog/nine.png", "blog/ten.png", "blog/ph-four.png", 7,
       "A look behind the curtain at the audits, shufflers and cameras that protect every hand and every spin.",
       [("Random Number Generators", ["All our slots and virtual table games use a certified Random Number Generator (RNG) that produces thousands of random outcomes every second. The RNG is tested by independent laboratories such as iTech Labs and GLI, and results are published in our fairness reports.", "Each spin is independent - previous results never influence future outcomes."]),
        ("Live Dealers & Equipment", ["Our live dealers use certified card shufflers and wheel balls that are inspected daily. Decks are replaced every few hours, and every card is scanned by optical character recognition (OCR) to transmit results to your screen.", "Cameras record every table and are kept for a minimum of 90 days."]),
        ("Your Protection", ["Our games are audited annually, and you can request the hand history of any round that you have played. If you believe a game was unfair, our support team will review the footage within 24 hours."])]),
    _p("goa-weekend-guide", "A Royal Weekend in Goa: Dining, Spa & the Gaming Floor", "Lifestyle", "25 Aug, 2026",
       "blog/four.png", "blog/eleven.png", "blog/ph-one.png", 21,
       "Plan a luxurious getaway on the banks of the Mandovi - from dawn yoga to midnight Baccarat.",
       [("Friday: Arrive in Style", ["Land at Dabolim or Mopa airport and be met by your chauffeur. Check in to your suite, freshen up at the Royale Spa, and enjoy a welcome cocktail on the riverside terrace.", "Dinner at 'Mehfil', our Mughlai fine-dining restaurant, is a must."]),
        ("Saturday: Explore & Play", ["Spend the day exploring Fontainhas, the Latin Quarter of Panaji, or take a sunset cruise on the Mandovi. In the evening, head to the gaming floor for a night at the tables, with live music in the Royale Lounge.", "Smart-casual dress is welcome on the floor; formal attire is requested in the Maharaja Salon."]),
        ("Sunday: Unwind", ["Sleep in, enjoy a Goan breakfast of poi and bhaji by the pool, and book a signature Ayurvedic massage. Check-out is at 2 pm for VIP members."])]),
    _p("understanding-rtp-volatility", "Understanding RTP and Volatility in Slots", "Guides", "18 Aug, 2026",
       "casino/b-slots-sq.svg", "casino/b-slots-wide.svg", "blog/ph-two.png", 11,
       "Two numbers every slot player should know before they spin.",
       [("What is RTP?", ["Return to Player (RTP) is the percentage of all wagers that a slot returns to players over millions of spins. A slot with an RTP of 96% will return ₹96 for every ₹100 wagered over the long term - and keep ₹4 as the house edge.", "RTP is a long-term average and says nothing about what will happen in a single session."]),
        ("What is Volatility?", ["Volatility (or variance) describes how wins are distributed. Low-volatility slots pay small wins frequently; high-volatility slots pay rarely but can pay very large amounts.", "Royal 777 Deluxe is medium-high volatility; Maharaja Megaways is high volatility."]),
        ("Choosing the Right Slot", ["If you want a long session on a small budget, choose a low-volatility slot with a high RTP. If you are chasing a big prize and can accept a bigger risk, choose a high-volatility game or a progressive jackpot.", "Always set your limits before you start spinning."])]),
]

BLOG_CATEGORIES = ["Strategy", "Guides", "Responsible Gaming", "VIP", "Events", "Fair Play", "Lifestyle"]
BLOG_TAGS = ["Teen Patti", "Roulette", "Blackjack", "Poker", "Slots", "Jackpot", "VIP", "Goa"]

# ---------------------------------------------------------------------------
# FAQs  (cat: account | payments | games | safety)
# ---------------------------------------------------------------------------
FAQ_CATS = [
    {"key": "all", "label": "All Questions", "icon": "ti-layout-grid"},
    {"key": "account", "label": "Account & KYC", "icon": "ti-user-check"},
    {"key": "payments", "label": "Payments", "icon": "ti-currency-rupee"},
    {"key": "games", "label": "Games", "icon": "ti-poker-chip"},
    {"key": "safety", "label": "Safety & Fair Play", "icon": "ti-shield-check"},
]

FAQS = [
    ("account", "Who can play at Casino Royale?", "Guests must be 21 years or older and hold a valid government-issued photo ID (Aadhaar, passport, driving licence or voter ID). Online play is available only in states and union territories where it is permitted by law. We reserve the right to restrict access based on your location."),
    ("account", "How do I create an account?", "Click 'Sign Up', enter your name, email and mobile number and verify the OTP sent to your phone. You will then be asked to complete KYC by uploading your PAN card and one more identity document. Verification is usually completed within 10 minutes."),
    ("account", "Why is KYC mandatory?", "As a casino we are a reporting entity under the Prevention of Money Laundering Act (PMLA), 2002. KYC lets us verify your age and identity, prevent fraud, and process your withdrawals securely. Your documents are encrypted and are never shared for marketing."),
    ("account", "I forgot my password. What should I do?", "Use the 'Forgot Password' link on the sign-in page and enter your registered mobile number or email. You will receive an OTP to reset your password. If you have no access to either, contact our support team on WhatsApp for assisted recovery."),
    ("payments", "Which payment methods are accepted?", "We accept UPI (Google Pay, PhonePe, Paytm and BHIM), net banking, IMPS, RuPay, Visa and Mastercard debit and credit cards. All transactions are in Indian Rupees (INR) and are processed through RBI-regulated payment partners."),
    ("payments", "How long do withdrawals take?", "UPI and IMPS withdrawals are typically completed within 15 to 30 minutes. Bank transfers (NEFT) can take up to 4 working hours. VIP members enjoy priority processing. Withdrawals can only be made to a bank account or UPI ID in your own name."),
    ("payments", "Is there a minimum deposit or withdrawal?", "The minimum deposit is ₹500 and the minimum withdrawal is ₹1,000. Daily withdrawal limits start at ₹5,00,000 and are increased for Gold, Platinum and Maharaja members."),
    ("payments", "Is TDS deducted on winnings?", "Yes. As per the Income Tax Act, tax at source (TDS) at 30% is deducted on net winnings above applicable thresholds. You can download your TDS certificate (Form 16A) from your account statement at the end of each financial quarter. Please consult a tax professional for your specific situation."),
    ("games", "What is the difference between Live Casino and Slots?", "Live Casino games like Teen Patti, Roulette and Blackjack are dealt by real dealers streamed live from our Goa gaming floor. Slots and jackpots are digital games driven by a certified random number generator (RNG)."),
    ("games", "Can I try games for free?", "Selected slots and the Keno game are available in 'Fun Mode' with virtual chips - no deposit required. Live dealer games require real-money play."),
    ("games", "How do jackpots work?", "Progressive jackpots grow with every qualifying bet across all tables and slots. When a player lands the jackpot, the prize is verified and paid in full, after which it resets to a seed amount. The current value is always shown on our Jackpots page."),
    ("games", "What are the bet limits?", "Limits vary by game: slots start at ₹10, live casino tables from ₹100 and VIP tables go up to ₹25,00,000 per round. The limits for each game are shown on its details page."),
    ("safety", "Are your games fair?", "Yes. All RNG games are certified by independent laboratories, and live games use certified shufflers, wheels and cameras. You can request the hand history of any round and our team will review it within 24 hours."),
    ("safety", "How is my data protected?", "We use 256-bit SSL encryption, two-factor authentication and strict access control. We comply with the Digital Personal Data Protection Act, 2023 and the Information Technology Act, 2000. See our Privacy Policy for more detail."),
    ("safety", "What tools help me play responsibly?", "You can set deposit, loss, wager and time limits, take a cool-off break from 24 hours to 6 months, or self-exclude for 1 to 5 years. Visit our Responsible Gaming page for details and helpline numbers."),
    ("safety", "How can I contact support?", "Our support team is available 24x7 on live chat, WhatsApp (+91 98905 12345), phone (+91 832 255 0188) and email (support@rajwaderoyale.in)."),
]

# ---------------------------------------------------------------------------
# Legal pages
# ---------------------------------------------------------------------------
PRIVACY = [
    ("privacyCategory", "ti-hand-finger", "Information We Collect", "All Categories", [
        "We collect information that you give us directly when you create an account, verify your identity, make a payment, contact support or take part in a promotion. This includes your name, date of birth, email address, mobile number, PAN and other identity documents, bank account or UPI details and your communication preferences.",
        "We also collect technical information automatically when you use our website and apps - such as your IP address, device identifiers, browser type, pages visited and approximate location (to enforce regional restrictions)."]),
    ("privacyInformation", "ti-info-circle", "How We Use Your Information", "Use of Information", [
        "We use your information to open and operate your account, verify that you are over 21, comply with anti-money-laundering (PMLA) and tax laws, process deposits and withdrawals, detect and prevent fraud, and offer customer support.",
        "With your consent, we send you promotional communications about tournaments, bonuses and events. You can opt out at any time from your account settings or by clicking 'unsubscribe' in any email."]),
    ("privacyShare", "ti-share", "Information Sharing & Disclosure", "Sharing & Disclosure", [
        "We do not sell your personal information. We share it only with payment partners, KYC providers, game studios (limited technical data), cloud-hosting providers and professional advisers who are bound by confidentiality obligations.",
        "We may disclose information to law-enforcement agencies, courts, tax authorities or regulators such as the Financial Intelligence Unit (FIU-IND) where the law requires, or to protect our rights and the safety of our guests."]),
    ("privacyRights", "ti-user", "Your Rights & Choices", "User Rights", [
        "Under the Digital Personal Data Protection Act, 2023 you have the right to access your data, to request corrections or erasure (subject to our legal retention duties), to withdraw consent, and to nominate another person to exercise your rights in case of death or incapacity.",
        "To exercise your rights, write to our Grievance Officer at privacy@rajwaderoyale.in. We will respond within 30 days."]),
    ("privacySecurity", "ti-lock", "Security Practices", "Security Practices", [
        "We protect your data with industry-standard safeguards: 256-bit TLS encryption in transit, AES-256 encryption at rest, role-based access, regular penetration testing and 24x7 monitoring. Payment card data is processed by PCI-DSS compliant partners and is never stored on our servers.",
        "Financial and KYC records are retained for five years after the closure of your account, as required by the PMLA. Other data is deleted or anonymised once it is no longer needed."]),
]

TERMS = [
    ("termsAcceptance", "ti-file-check", "Acceptance of Terms", "Acceptance", [
        "By creating an account, accessing our website or entering the Casino Royale premises, you agree to be bound by these Terms & Conditions, our Privacy Policy and our Responsible Gaming Policy. If you do not agree, please do not use our services.",
        "We may update these terms from time to time. Continued use of our services after changes are posted constitutes acceptance of the revised terms."]),
    ("termsEligibility", "ti-id", "Eligibility & Account", "Eligibility", [
        "You must be at least 21 years old, legally capable of entering into a binding contract, and resident in a jurisdiction where our services are lawful. You may hold only one account and must provide accurate information.",
        "We may suspend or close an account, withhold winnings or void bets if we find false information, multiple accounts, collusion, use of automated tools, or any other breach of these terms."]),
    ("termsDeposits", "ti-currency-rupee", "Deposits, Withdrawals & Taxes", "Payments", [
        "All transactions are in Indian Rupees. Deposits must be made from accounts in your own name, and withdrawals are paid to the same method used for deposits where possible. We may ask for additional verification before releasing large withdrawals.",
        "Winnings are subject to tax under the Income Tax Act, 1961. We deduct TDS where required and issue the relevant certificates. You are solely responsible for declaring your winnings and for any other tax liability."]),
    ("termsPlay", "ti-poker-chip", "Rules of Play & Bonuses", "Rules of Play", [
        "Each game is governed by its own rules, which are published on its details page. Bets are final once placed. In the event of a malfunction, all affected bets and payouts are void.",
        "Bonuses and promotions are subject to wagering requirements, expiry dates and maximum-win limits stated in the offer. Abuse of promotions, including bonus hunting, may result in forfeiture of the bonus and any winnings."]),
    ("termsConduct", "ti-shield-lock", "Fair Conduct, Liability & Disputes", "Conduct & Disputes", [
        "You agree not to use bots, collude with other players, exploit software errors or engage in money laundering. We cooperate fully with law-enforcement agencies in the investigation of unlawful activity.",
        "To the maximum extent permitted by law, our liability is limited to the amount of your account balance. Any dispute is first handled by our support team, then by our Grievance Officer, and finally by the courts at Panaji, Goa, under Indian law."]),
]

RESPONSIBLE = [
    ("rgCommitment", "ti-heart-handshake", "Our Commitment", "Our Commitment", [
        "Gaming should always be entertainment - never a way to make money or solve financial problems. At Casino Royale we are committed to providing a safe environment where our guests can enjoy the thrill of play while staying firmly in control.",
        "Our staff are trained to recognise signs of problem gambling and to help guests with limits, breaks and referrals. Entry to the gaming floor and registration online is restricted to adults aged 21 and over."]),
    ("rgLimits", "ti-adjustments", "Set Your Limits", "Set Limits", [
        "Set a budget before you play and stick to it. In your account you can set daily, weekly and monthly deposit limits; loss limits; wager limits; and session reminders that appear every 30, 60 or 120 minutes. Reductions take effect immediately; increases are delayed by 72 hours.",
        "On the floor, ask any host to help you set a spending limit or to arrange for a complimentary break with refreshments."]),
    ("rgWarning", "ti-alert-triangle", "Know the Warning Signs", "Warning Signs", [
        "You may be experiencing problems if you spend more time or money than you intended, chase your losses, borrow money to gamble, neglect work or family, or feel restless or irritable when not playing.",
        "If any of this sounds familiar, take a break and talk to someone you trust. The sooner you ask for help, the easier it is to recover."]),
    ("rgExclusion", "ti-ban", "Cool-off & Self-Exclusion", "Self-Exclusion", [
        "You can take a cool-off break of 24 hours, 7 days, 30 days or 6 months, or self-exclude for 1, 3 or 5 years. During exclusion your account is closed, marketing stops, and you are denied entry to our gaming floor.",
        "To start a cool-off or self-exclusion, use the 'Responsible Gaming' tab in your account, or email responsible@rajwaderoyale.in. Our team will confirm within 24 hours."]),
    ("rgHelp", "ti-lifebuoy", "Where to Get Help", "Get Help", [
        "Tele-MANAS (Government of India) offers free, confidential mental health support 24x7 on 14416 or 1800-891-4416. You can also contact local counselling services or speak to your family doctor.",
        "Our support team is available 24x7 at support@rajwaderoyale.in or +91 832 255 0188. We can also share information on blocking software, financial counselling and peer support groups."]),
]

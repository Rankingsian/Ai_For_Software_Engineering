import time

# 1. Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# 2. Chatbot Logic and Personality
print("Hey there! I'm CryptoBuddy, your friendly financial sidekick! 👋")
time.sleep(1)
print("I can help you find a green and growing crypto. 💰🌱")
time.sleep(1)
print("Here's a tip: You can ask about 'profitability' or 'sustainability'.")
time.sleep(1.5)

# A simple loop to keep the conversation going
while True:
    user_query = input("\nWhat's on your mind? (Type 'exit' to quit) 👉 ").lower()

    if user_query == 'exit':
        print("Thanks for chatting! Remember to always do your own research. Happy investing! 👋")
        break

    # 3. Add Advice Rules
    # Rule for Sustainability
    if "sustainable" in user_query or "eco-friendly" in user_query or "green" in user_query:
        # Filter for sustainable coins based on the rules
        sustainable_recommendations = [
            coin for coin, data in crypto_db.items()
            if data["energy_use"] == "low" and data["sustainability_score"] > 7/10
        ]

        if sustainable_recommendations:
            recommended_coin = sustainable_recommendations[0] # Pick the first one
            print(f"\n🌱 If sustainability is your top priority, consider {recommended_coin}! It has a low energy use and a high sustainability score. It's built for the long term!")
        else:
            print("\nI'm sorry, I don't have a coin that meets the sustainability criteria in my current database. 🤔")

    # Rule for Profitability
    elif "profit" in user_query or "buy" in user_query or "trending" in user_query:
        # Filter for profitable coins
        profitable_recommendations = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["market_cap"] == "high"
        ]

        if profitable_recommendations:
            recommended_coin = profitable_recommendations[0] # Pick the first one
            print(f"\n🚀 For short-term profitability, you might look at {recommended_coin}! It has a rising price trend and a high market cap.")
        else:
            print("\nBased on current data, I can't recommend a coin that meets the profitability criteria. 😕")

    # Rule for general recommendations
    elif "long-term growth" in user_query:
        # Combine rules for long-term growth (rising trend and sustainability)
        long_term_growth_coins = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["sustainability_score"] > 7/10
        ]

        if long_term_growth_coins:
            recommended_coin = long_term_growth_coins[0]
            print(f"\n📈 For long-term growth, you should check out {recommended_coin}! It's trending up and has an excellent sustainability score, making it a solid choice!")
        else:
            print("\nI'm sorry, I couldn't find a crypto that meets the criteria for both rising trend and high sustainability. 😔")

    # Fallback response for unhandled queries
    else:
        print("\nI'm not quite sure how to answer that. Could you try asking about 'profitability' or 'sustainability'? 🤔")
        
# 4. Ethics Alert
print("\n🚨 Disclaimer: Crypto is risky—always do your own research and consult with a financial advisor before making investment decisions.")
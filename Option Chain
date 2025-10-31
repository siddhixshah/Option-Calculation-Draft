# app.py
import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Option Algo Trap Simulation", layout="centered")

st.title("💹 Non-Liquid Option Simulation (Algo Trap)")

st.markdown("""
This app simulates a **non-liquid option scenario** where:
- The **algo acts as both buyer & seller**.
- It traps a normal buyer into buying **above the fair price**.
- After the trap, the algo resets quotes, leaving the buyer at a loss.
""")

st.sidebar.header("🔧 Simulation Parameters")

# Sidebar Inputs
fair_price = st.sidebar.slider("Fair Price of Option", 10.0, 200.0, 40.0, 1.0)
initial_bid = st.sidebar.slider("Initial Bid", 1.0, 100.0, 20.0, 1.0)
initial_ask = st.sidebar.slider("Initial Ask", 50.0, 200.0, 80.0, 1.0)
algo_restored_ask = st.sidebar.slider("Algo Restored Ask", 50.0, 200.0, 100.0, 1.0)
human_order_price = st.sidebar.slider("Early Human Order Price", 1.0, 200.0, 21.0, 1.0)
normal_buyer_arrival_step = st.sidebar.slider("Normal Buyer Arrival Step", 1, 50, 18, 1)
num_steps = st.sidebar.slider("Number of Simulation Steps", 10, 100, 25, 1)
algo_aggression = st.sidebar.slider("Algo Aggression (0–1)", 0.0, 1.0, 0.8, 0.1)
random_seed = st.sidebar.number_input("Random Seed", 0, 9999, 0, 1)

st.sidebar.markdown("---")
run_button = st.sidebar.button("▶️ Run Simulation")

if run_button:
    random.seed(random_seed)
    last_price = fair_price
    bid = initial_bid
    ask = initial_ask

    price_history = [last_price]
    time = [0]
    trades = []

    initial_human_order_placed = False
    victim_trade = None
    step_size = 1.0

    # Simulation Loop
    for t in range(1, num_steps + 1):
        if t == 1 and not initial_human_order_placed:
            initial_human_order_placed = True
            trades.append((t, human_order_price, 1, "early_human_limit_order_put"))

        if initial_human_order_placed and (last_price < fair_price * 1.1):
            delta = step_size * (0.2 + algo_aggression * random.random())
            last_price += delta
            trades.append((t, last_price, 1, "algo_buys_to_push"))
            bid = max(bid, last_price - 2.0)
            ask = max(ask, last_price + 10.0)
        else:
            last_price += (random.random() - 0.45) * 0.5

        if t == normal_buyer_arrival_step and victim_trade is None:
            trap_price = fair_price * 1.2
            victim_trade = (t, trap_price, 1, "normal_buyer_market_buy")
            trades.append(victim_trade)
            last_price = trap_price
            bid = initial_bid
            ask = algo_restored_ask

        price_history.append(last_price)
        time.append(t)

    # Output Summary
    st.subheader("📊 Simulation Summary")
    st.write(f"**Fair Price:** {fair_price}")
    st.write(f"**Initial Bid/Ask:** {initial_bid} / {initial_ask}")

    st.write("**Trades (Step, Price, Qty, Participant):**")
    st.table(trades)

    if victim_trade:
        t_v, price_v, qty_v, _ = victim_trade
        loss = price_v - fair_price
        st.error(f"💀 Victim bought at {price_v:.2f} (step {t_v}) → Loss = {loss:.2f} per unit")

    # Plot chart
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(time, price_history, marker='o', label="Last Price")
    ax.axhline(fair_price, linestyle='--', linewidth=1, color='gray', label="Fair Price")

    for tr in trades:
        step, price, qty, who = tr
        if who == "early_human_limit_order_put":
            ax.annotate("Early Human Order @21", xy=(step, price),
                        xytext=(step + 0.5, price - 6),
                        arrowprops=dict(arrowstyle="->", linewidth=0.8))
        elif who == "normal_buyer_market_buy":
            ax.annotate(f"Victim Buy (Algo Trap)\n@{price:.1f}", xy=(step, price),
                        xytext=(step - 6, price + 6),
                        arrowprops=dict(arrowstyle="->", linewidth=0.8))

    ax.set_xlabel("Simulation Step")
    ax.set_ylabel("Option Price")
    ax.set_title("Simulated Price Path: Algo Push-and-Sell Trap")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.caption("📈 This simulation is illustrative and not financial advice.")
else:
    st.info("👈 Adjust parameters on the sidebar and click **Run Simulation** to start.")

# app.py
import streamlit as st
import random

st.set_page_config(page_title="Option Algo Trap Simulation", layout="centered")

st.title("💹 Non-Liquid Option Simulation (Algo Trap)")

st.markdown("""
This app simulates a **non-liquid option** where:
- An **algo acts as both buyer and seller**.
- It traps a **normal buyer** by creating fake liquidity.
- After selling above the fair value, the algo resets quotes — leaving the buyer at a loss.
""")

# Sidebar Parameters
st.sidebar.header("🔧 Simulation Parameters")

fair_price = st.sidebar.slider("Fair Price of Option", 10.0, 200.0, 40.0, 1.0)
initial_bid = st.sidebar.slider("Initial Bid", 1.0, 100.0, 20.0, 1.0)
initial_ask = st.sidebar.slider("Initial Ask", 50.0, 200.0, 80.0, 1.0)
algo_restored_ask = st.sidebar.slider("Algo Restored Ask", 50.0, 200.0, 100.0, 1.0)
human_order_price = st.sidebar.slider("Early Human Order Price", 1.0, 200.0, 21.0, 1.0)
normal_buyer_arrival_step = st.sidebar.slider("Normal Buyer Arrival Step", 1, 50, 18, 1)
num_steps = st.sidebar.slider("Number of Simulation Steps", 10, 100, 25, 1)
algo_aggression = st.sidebar.slider("Algo Aggression (0–1)", 0.0, 1.0, 0.8, 0.1)
random_seed = st.sidebar.number_input("Random Seed", 0, 9999, 0, 1)

st.sidebar.m

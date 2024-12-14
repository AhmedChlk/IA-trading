# visualization.py

import matplotlib.pyplot as plt
import pandas as pd
import logging
import numpy as np

def plot_all_indicators(df, symbol):
    """
    Affiche un graphique combiné des indicateurs techniques.

    Args:
        df (pd.DataFrame): DataFrame contenant les données et les indicateurs.
        symbol (str): Symbole de trading (ex. 'BTCUSDT').
    """
    try:
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15, 24), sharex=True)
        
        # Prix de clôture
        ax1.plot(pd.to_datetime(df['timestamp'], unit='ms'), df['close'], label='Clôture', color='blue')
        ax1.set_title(f'{symbol} - Prix de Clôture')
        ax1.set_ylabel('Prix de Clôture (USDT)')
        ax1.legend()
        ax1.grid(True)
        
        # RSI
        ax2.plot(pd.to_datetime(df['timestamp'], unit='ms'), df['rsi'], label='RSI', color='orange')
        ax2.axhline(70, color='red', linestyle='--', label='Suracheté (70)')
        ax2.axhline(30, color='green', linestyle='--', label='Survendu (30)')
        ax2.set_title(f'{symbol} - Relative Strength Index (RSI)')
        ax2.set_ylabel('RSI')
        ax2.legend()
        ax2.grid(True)
        
        # Stochastic RSI
        ax3.plot(pd.to_datetime(df['timestamp'], unit='ms'), df['stochastic_k'], label='Stochastic K', color='blue')
        ax3.plot(pd.to_datetime(df['timestamp'], unit='ms'), df['stochastic_d'], label='Stochastic D', color='red')
        ax3.axhline(80, color='red', linestyle='--', label='Suracheté (80)')
        ax3.axhline(20, color='green', linestyle='--', label='Survendu (20)')
        ax3.set_title(f'{symbol} - Stochastic RSI (Stochastic K & Stochastic D)')
        ax3.set_ylabel('Stochastic RSI (%)')
        ax3.legend()
        ax3.grid(True)
        
        # ATR
        ax4.plot(pd.to_datetime(df['timestamp'], unit='ms'), df['atr'], label='ATR', color='magenta')
        ax4.set_title(f'{symbol} - Average True Range (ATR)')
        ax4.set_xlabel('Timestamp')
        ax4.set_ylabel('ATR')
        ax4.legend()
        ax4.grid(True)
        
        plt.tight_layout()
        plt.show()
        logging.info("Graphique combiné des indicateurs affiché avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la visualisation combinée des indicateurs : {e}")

def plot_predictions(train_true, train_pred, test_true, test_pred, n_steps, title='Prédictions vs Réel'):
    """
    Affiche un graphique des prédictions par rapport aux valeurs réelles pour les ensembles d'entraînement et de test.

    Args:
        train_true (np.ndarray): Valeurs réelles de l'ensemble d'entraînement.
        train_pred (np.ndarray): Prédictions de l'ensemble d'entraînement.
        test_true (np.ndarray): Valeurs réelles de l'ensemble de test.
        test_pred (np.ndarray): Prédictions de l'ensemble de test.
        n_steps (int): Nombre de pas de temps utilisés pour les séquences.
        title (str, optional): Titre du graphique. Par défaut à 'Prédictions vs Réel'.
    """
    try:
        plt.figure(figsize=(14,7))
        
        # Jeu d'entraînement
        plt.plot(train_true, label='Train Réel', color='green')
        plt.plot(train_pred, label='Train Prédit', color='orange')

        # Jeu de test
        offset = len(train_true)
        plt.plot(
            np.arange(offset, offset+len(test_true)), 
            test_true, 
            label='Test Réel', 
            color='blue'
        )
        plt.plot(
            np.arange(offset, offset+len(test_pred)), 
            test_pred, 
            label='Test Prédit', 
            color='red'
        )

        plt.title(title)
        plt.xlabel('Index Échantillon (Approx)')
        plt.ylabel('Prix de Clôture (Dénormalisé)')
        plt.legend()
        plt.grid(True)
        plt.show()
        logging.info("Graphique des prédictions affiché avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la visualisation des prédictions : {e}")

def plot_reward_history(reward_history):
    """
    Affiche un graphique de l'évolution des récompenses pendant l'entraînement.

    Args:
        reward_history (list): Liste des récompenses moyennes par époque.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(reward_history, label='Récompense Moyenne', color='purple')
        plt.xlabel('Époque')
        plt.ylabel('Récompense Moyenne')
        plt.title('Évolution des Récompenses pendant l\'Entraînement')
        plt.legend()
        plt.grid(True)
        plt.show()
        logging.info("Graphique de l'évolution des récompenses affiché avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors de la visualisation de l'évolution des récompenses : {e}")
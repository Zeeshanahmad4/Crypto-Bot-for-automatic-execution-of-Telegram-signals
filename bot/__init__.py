# bot/__init__.py

"""
The bot package is responsible for the core functionalities of the arbitrage trading bot. 
This includes reading signals from Telegram, executing trades on various cryptocurrency 
exchanges, and managing USDT funds.

Modules:
- signal_reader: For interpreting and acting upon signals received via Telegram.
- trade_executor: Handles the execution of trades on exchanges based on received signals.
- usdt_manager: Manages USDT for initial purchases and profit conversions, and alerts for low funds.
"""

# Importing the modules to make them accessible through the bot package.
# These imports assume that each module defines a class with the same name as the module.
from .signal_reader import SignalReader
from .trade_executor import TradeExecutor
from .usdt_manager import USDTManager

# Optionally, you could also define some shared utilities or common functions here
# that are used across multiple bot modules, if any exist.

# Defining an __all__ variable helps to restrict what is imported when
# from bot import * is used, and also serves as documentation for what
# the package is intended to expose.
__all__ = ['SignalReader', 'TradeExecutor', 'USDTManager']


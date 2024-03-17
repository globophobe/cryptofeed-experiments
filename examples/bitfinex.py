#!/usr/bin/env python3

from cryptofeed import FeedHandler
from cryptofeed.defines import TRADES

from quant_tick.exchanges import Bitfinex
from quant_tick.trades import (
    CandleCallback,
    NonSequentialIntegerTradeCallback,
    SignificantTradeCallback,
)


async def candles(candle: dict, timestamp: float) -> None:
    """Candles."""
    print(candle)


if __name__ == "__main__":
    fh = FeedHandler()
    fh.add_feed(
        Bitfinex(
            symbols=["BTCUSD"],
            channels=[TRADES],
            callbacks={
                TRADES: NonSequentialIntegerTradeCallback(
                    SignificantTradeCallback(
                        CandleCallback(candles, window_seconds=60),
                        significant_trade_filter=1_000,
                        window_seconds=60,
                    )
                )
            },
        )
    )
    fh.run()

#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# (c) ACE 

import os

class Config(object):

    # get a token from @BotFather

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6098387997:AAF0zipEzeLWiV04aslwdkdmuYfvwb1YFXg")

    API_ID = int(os.environ.get("API_ID", "29115376"))

    API_HASH = os.environ.get("API_HASH", "f1f760713aa29df4983cd7aef1b035a2")

    AUTH_USERS = "5269772"

#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2018
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains the ShippingQueryHandler class."""

from telegram import Update
from .handler import Handler


class ShippingQueryHandler(Handler):
    """Handler class to handle Telegram shipping callback queries.

    Attributes:
        callback (:obj:`callable`): The callback function for this handler.
        pass_update_queue (:obj:`bool`): Optional. Determines whether ``update_queue`` will be
            passed to the callback function.
        pass_job_queue (:obj:`bool`): Optional. Determines whether ``job_queue`` will be passed to
            the callback function.
        pass_user_data (:obj:`bool`): Optional. Determines whether ``user_data`` will be passed to
            the callback function.
        pass_chat_data (:obj:`bool`): Optional. Determines whether ``chat_data`` will be passed to
            the callback function.
        use_context (:obj:`bool`): Optional. Determines whether all `pass_` arguments will be
            ignored in favor of passing a :class:`telegram.ext.Context` object to the callback.

    Note:
        :attr:`pass_user_data` and :attr:`pass_chat_data` determine whether a ``dict`` you
        can use to keep any data in will be sent to the :attr:`callback` function.. Related to
        either the user or the chat that the update was sent in. For each update from the same user
        or in the same chat, it will be the same ``dict``.

    Note:
        Instead of using the individual `pass_` you can use :attr:`use_context` and your callback
        function will receive a :class:`telegram.ext.Context` object as the only parameter,
        instead of the usual (bot, update, others...).

    Args:
        callback (:obj:`callable`): A function that takes ``bot, update`` as positional arguments.
            It will be called when the :attr:`check_update` has determined that an update should be
            processed by this handler.
        pass_update_queue (:obj:`bool`, optional): If set to ``True``, a keyword argument called
            ``update_queue`` will be passed to the callback function. It will be the ``Queue``
            instance used by the :class:`telegram.ext.Updater` and :class:`telegram.ext.Dispatcher`
            that contains new updates which can be used to insert updates. Default is ``False``.
        pass_job_queue (:obj:`bool`, optional): If set to ``True``, a keyword argument called
            ``job_queue`` will be passed to the callback function. It will be a
            :class:`telegram.ext.JobQueue` instance created by the :class:`telegram.ext.Updater`
            which can be used to schedule new jobs. Default is ``False``.
        pass_user_data (:obj:`bool`, optional): If set to ``True``, a keyword argument called
            ``user_data`` will be passed to the callback function. Default is ``False``.
        pass_chat_data (:obj:`bool`, optional): If set to ``True``, a keyword argument called
            ``chat_data`` will be passed to the callback function. Default is ``False``.
        use_context (:obj:`bool`, optional): If set to ``True``, all `pass_` arguments will be
            ignored in favor of passing a :class:`telegram.ext.Context` object to the callback.
            Defaults to ``True`` if :attr:`callback` has only one parameter. Note that this can
            be difficult to determine if :attr:`callback` is decorated - especially on python 2.

    """

    def __init__(self,
                 callback,
                 pass_update_queue=False,
                 pass_job_queue=False,
                 pass_user_data=False,
                 pass_chat_data=False,
                 use_context=None):
        super(ShippingQueryHandler, self).__init__(
            callback,
            pass_update_queue=pass_update_queue,
            pass_job_queue=pass_job_queue,
            pass_user_data=pass_user_data,
            pass_chat_data=pass_chat_data,
            use_context=use_context)

    def check_update(self, update):
        """Determines whether an update should be passed to this handlers :attr:`callback`.

        Args:
            update (:class:`telegram.Update`): Incoming telegram update.

        Returns:
            :obj:`bool`

        """
        return isinstance(update, Update) and update.shipping_query

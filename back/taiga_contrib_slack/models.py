# Copyright (C) 2014-2016 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2016 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2016 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2016 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SlackHook(models.Model):
    project = models.ForeignKey("projects.Project", null=False, blank=False,
                                related_name="slackhooks")
    url = models.URLField(null=False, blank=False, verbose_name=_("URL"))
    channel = models.CharField(null=True, blank=True, verbose_name=_("Channel"), max_length=200)

    notify_issue_create = models.BooleanField(default=True)
    notify_issue_change = models.BooleanField(default=True)
    notify_issue_delete = models.BooleanField(default=True)

    notify_userstory_create = models.BooleanField(default=True)
    notify_userstory_change = models.BooleanField(default=True)
    notify_userstory_delete = models.BooleanField(default=True)

    notify_task_create = models.BooleanField(default=True)
    notify_task_change = models.BooleanField(default=True)
    notify_task_delete = models.BooleanField(default=True)

    notify_wikipage_create = models.BooleanField(default=True)
    notify_wikipage_change = models.BooleanField(default=True)
    notify_wikipage_delete = models.BooleanField(default=True)

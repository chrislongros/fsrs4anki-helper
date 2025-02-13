from aqt import mw

tag = mw.addonManager.addonFromModule(__name__)

LOAD_BALANCE = "load_balance"
EASY_DAYS = "easy_days"
EASY_DAYS_REVIEW_RATIO = "easy_days_review_ratio"
DAYS_TO_RESCHEDULE = "days_to_reschedule"
AUTO_RESCHEDULE_AFTER_SYNC = "auto_reschedule_after_sync"
AUTO_DISPERSE_AFTER_SYNC = "auto_disperse_after_sync"
AUTO_DISPERSE_WHEN_REVIEW = "auto_disperse_when_review"
AUTO_DISPERSE_AFTER_RESCHEDULE = "auto_disperse_after_reschedule"
MATURE_IVL = "mature_ivl"
DEBUG_NOTIFY = "debug_notify"
FSRS_STATS = "fsrs_stats"
DISPLAY_MEMORY_STATE = "display_memory_state"
AUTO_EASY_DAYS = "auto_easy_days"
HAS_RATED = "has_rated"


def load_config():
    return mw.addonManager.getConfig(tag)


def save_config(data):
    mw.addonManager.writeConfig(tag, data)


def run_on_configuration_change(function):
    mw.addonManager.setConfigUpdatedAction(__name__, lambda *_: function())


class Config:
    def load(self):
        self.data = load_config()

    def save(self):
        save_config(self.data)

    @property
    def load_balance(self):
        return self.data[LOAD_BALANCE]

    @load_balance.setter
    def load_balance(self, value):
        self.data[LOAD_BALANCE] = value
        self.save()

    @property
    def easy_days(self):
        return self.data[EASY_DAYS]

    @easy_days.setter
    def easy_days(self, day_enable):
        day, enable = day_enable
        if enable:
            self.data[EASY_DAYS] = sorted(set(self.data[EASY_DAYS] + [day]))
        else:
            if day in self.data[EASY_DAYS]:
                self.data[EASY_DAYS].remove(day)
        self.save()

    @property
    def easy_days_review_ratio(self):
        return max(0, min(self.data[EASY_DAYS_REVIEW_RATIO], 0.9))

    @easy_days_review_ratio.setter
    def easy_days_review_ratio(self, value):
        self.data[EASY_DAYS_REVIEW_RATIO] = max(0, min(value, 0.9))
        self.save()

    @property
    def days_to_reschedule(self):
        return self.data[DAYS_TO_RESCHEDULE]

    @days_to_reschedule.setter
    def days_to_reschedule(self, value):
        self.data[DAYS_TO_RESCHEDULE] = value
        self.save()

    @property
    def auto_reschedule_after_sync(self):
        return self.data[AUTO_RESCHEDULE_AFTER_SYNC]

    @auto_reschedule_after_sync.setter
    def auto_reschedule_after_sync(self, value):
        self.data[AUTO_RESCHEDULE_AFTER_SYNC] = value
        self.save()

    @property
    def auto_disperse_after_sync(self):
        return self.data[AUTO_DISPERSE_AFTER_SYNC]

    @auto_disperse_after_sync.setter
    def auto_disperse_after_sync(self, value):
        self.data[AUTO_DISPERSE_AFTER_SYNC] = value
        self.save()

    @property
    def auto_disperse_when_review(self):
        return self.data[AUTO_DISPERSE_WHEN_REVIEW]

    @auto_disperse_when_review.setter
    def auto_disperse_when_review(self, value):
        self.data[AUTO_DISPERSE_WHEN_REVIEW] = value
        self.save()

    @property
    def auto_disperse_after_reschedule(self):
        return self.data[AUTO_DISPERSE_AFTER_RESCHEDULE]

    @auto_disperse_after_reschedule.setter
    def auto_disperse_after_reschedule(self, value):
        self.data[AUTO_DISPERSE_AFTER_RESCHEDULE] = value
        self.save()

    @property
    def mature_ivl(self):
        return self.data[MATURE_IVL]

    @mature_ivl.setter
    def mature_ivl(self, value):
        self.data[MATURE_IVL] = value
        self.save()

    @property
    def debug_notify(self):
        return self.data[DEBUG_NOTIFY]

    @debug_notify.setter
    def debug_notify(self, value):
        self.data[DEBUG_NOTIFY] = value
        self.save()

    @property
    def fsrs_stats(self):
        return self.data[FSRS_STATS]

    @fsrs_stats.setter
    def fsrs_stats(self, value):
        self.data[FSRS_STATS] = value
        self.save()

    @property
    def display_memory_state(self):
        return self.data[DISPLAY_MEMORY_STATE]

    @display_memory_state.setter
    def display_memory_state(self, value):
        self.data[DISPLAY_MEMORY_STATE] = value
        self.save()

    @property
    def auto_easy_days(self):
        return self.data[AUTO_EASY_DAYS]

    @auto_easy_days.setter
    def auto_easy_days(self, value):
        self.data[AUTO_EASY_DAYS] = value
        self.save()

    @property
    def has_rated(self):
        return self.data[HAS_RATED]

    @has_rated.setter
    def has_rated(self, value):
        self.data[HAS_RATED] = value
        self.save()

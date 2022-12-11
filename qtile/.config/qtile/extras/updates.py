from subprocess import CalledProcessError, Popen

from libqtile.widget import base


class CheckUpdates(base.ThreadPoolText):
    CMD_DICT = {
        "pacman": "checkupdates",
        "paru": "paru -Qu",
    }

    def __init__(
        self,
        distro: dict,
        initial_text: str = "",
        update_interval: int = 3600,
        display_format="Updates {updates}",
        no_update_string="Sistema Actualizado",
        execute=None,
        **config,
    ) -> None:
        base.ThreadPoolText.__init__(self, config.pop("initial_text", ""), **config)
        self.add_defaults(CheckUpdates.defaults)

        self.distro = distro or self.CMD_DICT
        self.initial_text = initial_text
        self.update_interval = update_interval
        self.display_format = display_format
        self.no_update_string = no_update_string
        self.execute = execute

        if self.execute:
            self.add_callbacks({"Button1": self.do_execute})

        self.updates = {}

    def _check_updates(self) -> str:
        try:
            updates = 0
            for repo, cmd in self.distro.items():
                update = self.call_process(cmd, shell=True)
                self.updates[repo] = update
                updates += len(update.splitlines())
        except CalledProcessError:
            updates = -1

        if self.layout:
            if updates == 0:
                self.layout.colour = self.colour_no_updates
                return self.no_update_string

            self.layout.colour = self.colour_have_updates

        return self.display_format.format(**{"updates": updates})

    def poll(self) -> str:
        return self._check_updates()

    def do_execute(self) -> None:
        if self.execute:
            self._process = Popen(self.execute, shell=True)
            self.timeout_add(self.execute_polling_interval, self._refresh_count)

    def _refresh_count(self):
        if self._process.poll() is None:
            self.timeout_add(self.execute_polling_interval, self._refresh_count)

        else:
            self.timer_setup()

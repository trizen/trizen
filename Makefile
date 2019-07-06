BUGADDR   = Trizen <echo dHJpemVuQHByb3Rvbm1haWwuY29tCg== | base64 -d>
COPYRIGHT = Copyright (C) 2010-2019 $(BUGADDR).

EXENAME ?= trizen
BINVER  ?= 1.58.13

PREFIX  ?= /usr/local
DESTDIR ?=

BINDIR ?= $(DESTDIR)$(PREFIX)/bin
MANDIR ?= $(DESTDIR)$(PREFIX)/share/man/man1
MODIR  ?= $(DESTDIR)$(PREFIX)/share/locale

COMP_BASHDIR ?= $(DESTDIR)$(PREFIX)/share/bash-completion/completions
COMP_FISHDIR ?= $(DESTDIR)$(PREFIX)/share/fish/vendor_completions.d
COMP_ZSHDIR  ?= $(DESTDIR)$(PREFIX)/share/zsh/site-functions

COMP ?= bash.completion fish.completion zsh.completion
PO   ?=

INSTALL_EXE  ?= install -D --mode=755
INSTALL_DATA ?= install -D --mode=644
RM           ?= rm -f
MSGFMT       ?= msgfmt --check --statistics --verbose
FXGETTEXT    ?= --width=80 --no-wrap
MSGMERGE     ?= msgmerge $(FXGETTEXT) --update --backup=existing --verbose
XGETTEXT     ?= xgettext $(FXGETTEXT) --from-code=UTF-8 --add-comments="TRANSLATION:" --keyword="__" \
				--keyword="__x" --keyword="__px:1c,2" --keyword="__p:1c,2" --keyword="__n:1,2"       \
				--language=Perl --copyright-holder="$(COPYRIGHT)" --package-name="$(EXENAME)"        \
				--package-version=$(BINVER) --msgid-bugs-address="$(BUGADDR)"

.PHONY: all
all: $(PO:.po=.mo)

i18n/$(EXENAME).pot: $(EXENAME)
	@echo "Creating the Portable Object Template file: $@..."
	$(XGETTEXT) $< -o $@

i18n/%.po: $(EXENAME).pot
	@echo "Merging the Portable Object Template file into $@..."
	$(MSGMERGE) $@ $<

i18n/%.mo: i18n/%.po
	@echo "Compiling the Portable Object file: $<..."
	$(MSGFMT) $< -o $@

.PHONY: install
install: all
	@echo "Installing the executable..."
	$(INSTALL_EXE) "$(EXENAME)" "$(BINDIR)/$(EXENAME)"
	@echo "Installing the man page..."
	$(INSTALL_DATA) "$(EXENAME).1" "$(MANDIR)/$(EXENAME).1"
	@echo "Installing the Machine Object files..."
	for i in $(notdir $(basename $(PO))); do \
		$(INSTALL_DATA) "i18n/$$i.mo" "$(MODIR)/$$i/LC_MESSAGES/$(EXENAME).mo"; \
	done
	@echo "Installing the completion files..."
	for i in $(COMP); do \
		case $$i in \
			*bash*) \
				$(INSTALL_DATA) "$$i" "$(COMP_BASHDIR)/$(EXENAME)" ;; \
			*fish*) \
				$(INSTALL_DATA) "$$i" "$(COMP_FISHDIR)/$(EXENAME).fish" ;; \
			*zsh*) \
				$(INSTALL_DATA) "$$i" "$(COMP_ZSHDIR)/_$(EXENAME)" ;; \
		esac \
	done

.PHONY: uninstall
uninstall:
	@echo "Uninstalling the executable..."
	$(RM) "$(BINDIR)/$(EXENAME)"
	@echo "Uninstalling the man page..."
	$(RM) "$(MANDIR)/$(EXENAME).1"
	@echo "Uninstalling the Machine Object files..."
	for i in $(notdir $(basename $(PO))); do \
		$(RM) "$(MODIR)/$$i/LC_MESSAGES/$(EXENAME).mo"; \
	done
	@echo "Uninstalling the completion files..."
	for i in $(COMP); do \
		case $$i in \
			*bash*) \
				$(RM) "$(COMP_BASHDIR)/$(EXENAME)" ;; \
			*fish*) \
				$(RM) "$(COMP_FISHDIR)/$(EXENAME).fish" ;; \
			*zsh*) \
				$(RM) "$(COMP_ZSHDIR)/_$(EXENAME)" ;; \
		esac \
	done

.PHONY: clean
clean:
	@echo "Deleting all Machine Object files..."
	$(RM) i18n/*.mo
	@echo "Deleting all Portable Object backups..."
	$(RM) i18n/*.po~

.PHONY: mrproper
mrproper: clean
	@echo "Deleting the Portable Object Template file..."
	$(RM) i18n/$(EXENAME).pot

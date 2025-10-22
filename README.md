# 0711 Smart Home Fernwartungs Modus

[![HACS ICON](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/0711smarthome/0711smarthome_fernwartungs_modus)](https://github.com/0711smarthome/0711smarthome_fernwartungs_modus/releases/latest)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/0711smarthome/0711smarthome_fernwartungs_modus)](https://github.com/0711smarthome/0711smarthome_fernwartungs_modus)

Diese Custom Component für Home Assistant ermöglicht es, einen spezifischen Admin-Benutzer über einen einfachen Schalter (Switch) zu aktivieren und zu deaktivieren. Dies ist ideal für die **sichere, temporäre Fernwartung** Ihres Home Assistant Systems.

**Hauptfunktion:** Aktivieren oder deaktivieren Sie den Fernwartungs-Admin-Account, ohne sich ständig manuell ab- und anmelden zu müssen.

---

## 🚀 Installation via HACS (Empfohlen)

Die einfachste Methode zur Installation ist über den Home Assistant Community Store (HACS).

1.  **HACS öffnen:** Navigieren Sie in Home Assistant zu **HACS**.
2.  **Benutzerdefiniertes Repository hinzufügen:**
    * Klicken Sie auf den Reiter **"Integrationen"**.
    * Klicken Sie oben rechts auf das **Drei-Punkte-Menü** ($\dots$) und wählen Sie **"Benutzerdefinierte Repositorys"**.
3.  **Details eingeben:**
    * **Repository:** `0711smarthome/0711smarthome_fernwartungs_modus`
    * **Kategorie:** `Integration`
4.  Klicken Sie auf **Hinzufügen**.
5.  **Installieren & Neustart:** Suchen Sie die Integration in HACS, klicken Sie auf **Download** und starten Sie Home Assistant neu.

---

## 🛠️ Konfiguration

Nach dem Neustart wird die Integration konfiguriert:

1.  Gehen Sie zu **Einstellungen** ($\text{Zahnrad}$) > **Geräte & Dienste**.
2.  Klicken Sie auf **Integration hinzufügen** ($\mathbf{+}$).
3.  Suchen Sie nach **"0711 Smart Home Fernwartungs Modus"**.
4.  **Admin-Benutzer auswählen:** Wählen Sie im Konfigurationsdialog den Administrator-Account aus, den Sie über den Schalter steuern möchten (dies sollte der Account für die Fernwartung sein).

**Wichtig:** Der Benutzer, den Sie auswählen, darf **nicht** der Benutzer sein, mit dem Sie die Konfiguration gerade durchführen.

---

## 💡 Nutzung

Nach erfolgreicher Konfiguration wird ein neuer **Switch-Entität** erstellt:

* **Entität-ID (Beispiel):** `switch.admin_user_toggle_xyz`

### Zustände

| Zustand | Admin-Benutzer | Bedeutung |
| :--- | :--- | :--- |
| **ON** | Aktiviert | Der Fernwartungs-Admin kann sich anmelden. |
| **OFF** | Deaktiviert | Der Fernwartungs-Admin kann sich **nicht** anmelden (Sicherheit). |

Verwenden Sie diesen Schalter in Ihren Dashboards oder Automatisierungen.

---

## 🐞 Support und Fehler melden

Sollten Sie Probleme mit dieser Integration haben, nutzen Sie bitte den offiziellen Issue Tracker:

* **Issue Tracker:** [https://0711smarthome.de](https://0711smarthome.de)

---
*Codeowners: [@0711smarthome](https://github.com/0711smarthome)*

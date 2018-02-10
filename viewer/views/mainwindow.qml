import QtQuick 2.7
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3

ApplicationWindow {
    id: rootWindow
    visible: true
    width: 640
    height: 240
    title: qsTr("Codes viewer")
    color: "whitesmoke"

    ColumnLayout {
        spacing: 2

        ListModel {
            id: codesComboboxModel
        }

        ComboBox {
            id: codesCombobox;
            editable: true;
            model: codesComboboxModel
            textRole: 'text'
            delegate: codesComboboxDelegate
            onAccepted: {
                mainwindowVm.search(codesCombobox.editText)
            }
            onActivated: {
                mainwindowVm.selected_code_changed(codesComboboxModel.get(index).value)
            }
        }
        Text {
            id: descriptionText;
        }
    }

    Connections {
        target: mainwindowVm

        // signal handler
        onSearchStringResult: {
            codesComboboxModel.clear()
            for (var i = 0; i < mainwindowVm.codes.length; i++) {
                codesComboboxModel.append({text:  mainwindowVm.codes[i].code, value : mainwindowVm.codes[i]})
            }
        }
        onSelectedCodeChanged: {
            descriptionText.text = mainwindowVm.selected_code.description
        }
    }
}


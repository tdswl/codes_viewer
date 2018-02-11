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
        anchors.margins: 10
        anchors.fill: parent

        ListModel {
            id: codesComboboxModel
        }

        Text {
            font.pointSize: 15
            text: "Code:"
        }

        ComboBox {
            id: codesCombobox
            Layout.fillWidth: true
            editable: true
            font.pointSize: 12
            model: codesComboboxModel
            textRole: "text"
            onAccepted: {
                mainwindowVm.search(codesCombobox.editText)
            }
            onActivated: {
                mainwindowVm.selected_code_changed(codesComboboxModel.get(index).value)
            }
        }

        Text {
            Layout.topMargin: 10
            font.pointSize: 15
            text: "Description:"
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            border.width: 1
            border.color: "#e0e0e0"
            color: "white"

            TextArea {
                id: descriptionText;
                font.pointSize: 12
                anchors.fill: parent
                selectByMouse: true
                selectByKeyboard: true
                readOnly: true
            }
        }
    }

    Connections {
        target: mainwindowVm

        // signal handler
        onSearchStringResult: {
            codesComboboxModel.clear()
            if (mainwindowVm.codes.length)
            {
                for (var i = 0; i < mainwindowVm.codes.length; i++) {
                    codesComboboxModel.append({text:  mainwindowVm.codes[i].code, value : mainwindowVm.codes[i]})
                }
                codesCombobox.popup.activeFocus = true
                codesCombobox.popup.open()
            }
        }
        onSelectedCodeChanged: {
            descriptionText.text = mainwindowVm.selected_code.description
        }
    }
}


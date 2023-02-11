const vscode = require("vscode");

function activate() {
  vscode.window.showInformationMessage("SugarCode插件已启动!");
}

function deactivate() {
  vscode.window.showWarningMessage("SugarCode插件已退出!");
}

module.exports = {
  activate,
  deactivate,
};

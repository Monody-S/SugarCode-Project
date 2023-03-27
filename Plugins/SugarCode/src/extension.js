const vscode = require("vscode");

function activate() {
  vscode.languages.registerDocumentFormattingEditProvider("SugarCode", {
    provideDocumentFormattingEdits(document) {
      let changes = [];
      let inSting = false;
      let inComment = false;
      for (let n = 0; n < document.lineCount; n++) {
        let flag = false;
        let line = document.lineAt(n);
        let content = line.text;
        let string = "";
        for (let index = 0; index < content.length; index++) {
          let char = content[index];
          if (char == "#" && !inSting) {
          } else if (char == '"' && content[index - 1] != "\\") {
            inSting = !inSting;
          }
          if (inComment || inSting) {
            string += char;
            continue;
          }
          if (char == " ") {
            continue;
          } else if (char == "|") {
            string += " | ";
            continue;
          } else if (char == ">") {
            if (flag) {
              string += "\n";
            }
            string += "    ";
            flag = true;
          } else if (char == "@") {
            if (
              document.lineAt(n - 1).text.replace(/#.*?#/g, "") &&
              content[index + 1] == "条" &&
              content[index + 2] == "件"
            ) {
              string += "\n";
            }
            flag = true;
          }
          string += char;
        }
        if (string != content) {
          changes.push(vscode.TextEdit.replace(line.range, string));
        }
      }
      let lastLine = document.lineAt(document.lineCount - 1);
      if (lastLine.text != "") {
        changes.push(vscode.TextEdit.insert(lastLine.range.end, "\n"));
      }
      return changes;
    },
  });
}

module.exports = { activate };

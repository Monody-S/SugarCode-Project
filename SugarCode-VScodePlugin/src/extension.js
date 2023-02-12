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
        let content = line.text.replace(/\s/g, "");
        let string = "    ";
        if (content == "" || content[0] == "@") {
          string = "";
        }
        for (let index = 0; index < content.length; index++) {
          const char = content[index];
          if (char == "#" && !inSting) {
            inComment = !inComment;
          }
          if (char == '"' && content[index - 1] !== "\\" && !inComment) {
            inSting = !inSting;
          }
          if (!inSting && !inComment) {
            if (char == "|") {
              string += " | ";
              continue;
            } else if (char == ">") {
              if (flag) {
                string += "\n    >";
                continue;
              }
              flag = true;
            } else if (char == "@") {
              flag = true;
            }
          }
          string += char;
        }
        changes.push(vscode.TextEdit.replace(line.range, string));
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

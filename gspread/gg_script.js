function myFunction() {
    const mappings = [
      { source: 'baby_male', target: 'baby_male_formatted' },
      { source: 'baby_female', target: 'baby_female_formatted' }
    ];
    mappings.forEach(pair => {
      createFormattedSheetFromMale(pair.source, pair.target);
    });
  }
  
  function createFormattedSheetFromMale(sheetName, targetName) {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sourceSheet = ss.getSheetByName(sheetName);
    const targetSheetName = targetName;
  
    const oldSheet = ss.getSheetByName(targetSheetName);
    if (oldSheet) ss.deleteSheet(oldSheet);
  
    const newSheet = ss.insertSheet(targetSheetName);
  
    const data = sourceSheet.getRange(2, 1, sourceSheet.getLastRow() - 1, 2).getValues();
    const totalItems = data.length;
  
    const headerRow1 = [totalItems, '', 0, 0];
    const headerRow2 = ['item_id', 'thumbnail', 'select', 'review'];
  
    newSheet.getRange(1, 1, 1, 4).setValues([headerRow1]);
    newSheet.getRange(2, 1, 1, 4).setValues([headerRow2]);
  
    newSheet.getRange("A1:D2").setFontWeight("bold").setBackground("yellow");
  
    const output = data.map(row => {
      const itemId = row[0];
      const idStr = itemId.toString().padStart(9, '0');
      const imageFormula = `=IMAGE("https://t.pimg.jp/${idStr.substring(0,3)}/${idStr.substring(3,6)}/${idStr.substring(6,9)}/1/${itemId}.jpg",1)`;
      return [itemId, imageFormula, 0, 0];
    });
  
    newSheet.getRange(3, 1, output.length, 4).setValues(output);
    newSheet.getRange(2, 1, newSheet.getLastRow() - 1, 4).createFilter();
  
    newSheet.setColumnWidth(1, 100);  
    newSheet.setColumnWidth(2, 300); 
    newSheet.setRowHeights(3, output.length, 300);
    newSheet.setColumnWidth(3, 100); 
    newSheet.setColumnWidth(4, 100); 
  }
  
  
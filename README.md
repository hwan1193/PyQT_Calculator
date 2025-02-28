PyQt에서는 디자이너(Designer) 툴과 스타일 시트(StyleSheet), 내장 스타일 등을 활용해 UI를 예쁘게 꾸밀 수 있습니다. 현재 코드 기반으로 작업한다면, 아래와 같은 방법들을 시도해볼 수 있습니다.

1. Qt Designer에서 레이아웃 및 스타일 조정
Qt Designer로 pyqtUI.ui 파일을 열어서, 각 버튼과 레이아웃의 간격(margin, spacing), 크기 정책(sizePolicy), 폰트 등을 조정할 수 있습니다.
Qt Designer의 Object Inspector에서 버튼들을 선택 후, Property 창에서 font, styleSheet, sizePolicy, alignment 등을 조정할 수 있습니다.
예쁘게 만들려면, 버튼의 간격과 여백(layout margin/spacing)을 충분히 주고, 글자 크기(font size)와 색상을 조정하는 것만으로도 훨씬 깔끔해집니다.
2. 스타일 시트(Style Sheet) 적용
PyQt에서는 CSS와 유사한 **스타일 시트(StyleSheet)**를 적용하여 색상, 테두리, 배경, 폰트 등을 꾸밀 수 있습니다.

# Github Header 꾸미기

## 기본 사용 방법

**Markdown**

```md
![header](https://capsule-render.vercel.app/api?)
```

**HTML**

```html
<img src="https://capsule-render.vercel.app/api? />
```

## 모양

1. wave(default)
2. egg
3. shark
4. slice
5. rect
6. soft
7. rounded
8. cylinder
9. waving
10. venom
11. transparent

### 사용예시

**Markdown**

`![header](https://capsule-render.vercel.app/api?type=wave)`

**HTML**

`<img src="https://capsule-render.vercel.app/api?type=wave />`


## 색상
`color=`

- **auto: 자동 색상 무작위 변경**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=auto)`

    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=auto />`

- **timeAuto: 시간에 따라 무작위 색상 변경**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=timeAuto)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=timeAuto />`
- **random: 무작위 색상**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=random)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=random />`
- **gradient: 그라데이션**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=gradient)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=gradient />`

- **timeGradient: 시간에 따라 그라데이션**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=timeGradient)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=timeGradient />`
- **_hexcode: 기본값(#B897FF)**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF />`

- **_custom_gradient: 사용자 정의 그라데이션**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8 />`

## 부분(섹션)

`section=`

- **header: (기본)**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=header)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=header />`

- **footer**

    **MarkDown**

    `![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer)`
    
    **HTML**

    `<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer />`


## 높이
`height=`: default 120

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer&height=100)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=0:B897FF,100:a82da8&section=footer&height=100 />`

## 텍스트
`text=`

- `%20`: 공백

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘%20셋)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘%20셋 />`

- `-nl-`: 줄바꿈

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋 />`

## 설명(줄 추가)

`desc=`

* 특수문자 사용 불가
* 일반적으로 공백(%20)만 사용함

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글 />`

## 텍스트 애니메이션

`animation=`
- **fadeIn: 페이드인 1.2초**

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=fadeIn)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=fadeIn />`

- **scaleIn: 날라옴 0.8초**

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=scaleIn)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=scaleIn />`

- **blink: 깜박임 0.6초**

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blink)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blink />`

- **blinking: 깜박임 1.6초**

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blinking)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=blinking />`

- **twinkling: 반짝임 4초**

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=twinkling)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=하나둘-nl-셋&desc=설명글&animation=twinkling />`


## 제목 글자 색상
`fontColor=`

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000 />`

- 값은 "#"없이 16진수 코드여야 함
- 텍스트쿼리 뒤에 쓰기


## 제목 글자 크기

`fontSize=`default = 70

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50 />`

- 텍스트 쿼리 뒤에 쓰기

## 제목 글자 위치 조정

### x축 조정
`fontAlign=`default 50

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlign=20)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlign=20 />`

### y축 조정
`fontAlignY=`default 50

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlignY=20)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&text=제%20목&fontColor=000000&fontSize=50&fontAlignY=20 />`

## 설명 글자 크기

`descSize=`default = 20

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50 />`

- desc쿼리 뒤에 쓰기


## 설명 위치 조정

### x축 조정
`descAlign=`default 50

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlign=30)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlign=30 />`

### y축 조정
`descAlignY=`default 50

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30 />`

## 회전
`rotate=`(-360 ~ 360)

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30&rotate=60)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&desc=설명글&descSize=50&descAlignY=30&rotate=60 />`

## 텍스트 외곽 선

### 글자 외곽 색상 변경
`stroke=`

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845 />`

- #이 없는 16진수 색상코드

### 글자 외곽 색상 폭

`strokeWidth=`

  **MarkDown**

  `![header](https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845&strokeWidth=3)`
  
  **HTML**

  `<img src="https://capsule-render.vercel.app/api?type=wave&color=B897FF&fontColor=1111&text=글%20자&stroke=888845&strokeWidth=3 />`

- stroke 쿼리 뒤에 쓰기
BaseWidth := 1280
BaseHeight := 768
YourWidth := 1920
YourHeight := 1080
F1::
Games := 0
Loop
{
  Menu, Tray, Tip, Total games played - %Games%
  w.__handle
  Loop
  {
    PixelGetColor, pixcolor, 167 * YourWidth / BaseWidth, 686 * YourHeight / BaseHeight
    If (pixcolor = 0xf0f0f0) {
      Mouseclick, left, 157 * YourWidth / BaseWidth, 719 * YourHeight / BaseHeight
      sleep, 500
    }
  } until pixcolor != 0xf0f0f0
  Loop
  {
    PixelGetColor, pixcolor2, 1265 * YourWidth / BaseWidth, 679 * YourHeight / BaseHeight
    If !(pixcolor2 = 0x00FFFF) {
      Mouseclick, left, 604 * YourWidth / BaseWidth, 32 * YourHeight / BaseHeight
      Mouseclick, left, 866 * YourWidth / BaseWidth, 24 * YourHeight / BaseHeight
      Mouseclick, left, 727 * YourWidth / BaseWidth, 23 * YourHeight / BaseHeight
      sleep, 500
    }
  } until pixcolor2 = 0x00FFFF
  Loop
  {
    PixelGetColor pixcolor3, 602 * YourWidth / BaseWidth, 100 * YourHeight / BaseHeight
    PixelGetColor pixcolor5, 1061 * YourWidth / BaseWidth, 21 * YourHeight / BaseHeight
    Send, {W down}
    sleep, 300
    Send, {W up}
    Send, {S down}
    sleep, 300
    Send, {S up}
    Send, {A down}
    sleep, 300
    Send, {A up}
    Send, {D down}
    sleep, 300
    Send, {D up}
    sleep, 200
    Send, {Q}
    sleep, 500
    Send, {Z}
    Mouseclick, left
  } until pixcolor3 = 0xE8E8FF or pixcolor5 = 0xF0F0F0
  Send, {Space}
  sleep, 100
  Mouseclick left, 568 * YourWidth / BaseWidth, 503 * YourHeight / BaseHeight
  Loop
  {
    PixelGetColor, pixcolor4, 167 * YourWidth / BaseWidth, 686 * YourHeight / BaseHeight
    Send, {Space}
    sleep, 100
  } until pixcolor4 = 0xf0f0f0
  Games := Games + 1
}
return
 
F2::
Pause, Toggle

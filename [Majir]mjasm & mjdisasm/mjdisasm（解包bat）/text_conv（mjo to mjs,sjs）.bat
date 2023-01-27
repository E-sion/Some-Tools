for %%a in (*.mjo) do (
  md "%%~na"
  mjdisasm "%%~a"
  move "%%~na.mjs" "%%~na"
  move "%%~na.sjs" "%%~na"
)
puase
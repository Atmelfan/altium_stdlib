# altium_stdlib
Standard Altium library

Note: Libraries actives and connectors are deprecated. Do not add new components, instead add to their respective manufacturer.

The library lib_passives are partially deprecated, any non-standard package or part should be added to their respective manufacturer instead. Passives in standard packages can still be used.

Lägg bibliotek i undermappar typ lib_whatever.
Lägg sedan till genererade intlibs i andra projekt 

T.ex:
* lib_passives:
  * Project outputs for lib_passives:
    * lib_passives.IntLib
  * lib_passives.LibPkg
  * lib_passives.SchLib
  * lib_passives.PcbLib

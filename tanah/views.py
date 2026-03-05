import matplotlib
matplotlib.use('Agg')  # penting untuk Django
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .fuzzy import kualitas_tanah_fuzzy

def form_input(request):
    if request.method == 'POST':
        pH = float(request.POST['pH'])
        KTK = float(request.POST['KTK'])
        Corg = float(request.POST['C_Organik'])
        N = float(request.POST['N_Total'])
        P = float(request.POST['P_Total'])
        K = float(request.POST['K_Total'])

        hasil = kualitas_tanah_fuzzy(pH, KTK, Corg, N, P, K)

        label = {
            0: "Tidak Sehat",
            1: "Kurang Sehat",
            2: "Sehat"
        }

        # =========================
        # Buat Radar Chart
        # =========================
        labels = ['pH', 'KTK', 'C-Organik', 'N-Total', 'P-Total', 'K-Total']
        values = np.array([pH, KTK, Corg, N, P, K])
        
        # Normalisasi agar visual proporsional
        values = values / values.max()
        
        values = np.concatenate((values, [values[0]]))
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.set_yticklabels([])
        ax.set_title("Grafik Radar Kualitas Tanah")
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        plt.close(fig)

        return render(request, 'tanah/result.html', {
            'hasil': hasil,
            'label': label[hasil],
            'graphic': graphic
        })

    return render(request, 'tanah/form.html')

package src.com.Geradengleichung;

public class mainFile {

	public static void main(String[] args) {

		
		// Gerade 1
		
		float PunktX1, PunktX2, PunktX3;
		PunktX1 = 1;
		PunktX2 = 0;
		PunktX3 = 5;
		
		float RVX1, RVX2, RVX3;
		RVX1 = 2;
		RVX2 = -2;
		RVX3= 2;
		
		
		// Gerade 2
		
		float Punkt2X1, Punkt2X2, Punkt2X3;
		Punkt2X1 = 5;
		Punkt2X2 = 0;
		Punkt2X3 = 1;
		
		float RV2X1, RV2X2, RV2X3;
		RV2X1 = -3;
		RV2X2 = 3;
		RV2X3= -3;
		
		//if parallel -> Identisch
		
		// Parallel prüfung
		
		float RVDIVX1, RVDIVX2, RVDIVX3;
		RVDIVX1 = RVX1/RV2X1;
		RVDIVX2 = RVX2/RV2X2;
		RVDIVX3 = RVX3/RV2X3;
		
		
		// isTRUE2 ist 1 = Parallel; 0 = Nicht parallel
		int isTRUE = 0;
		int isTRUE2 = 0;
		
		if (RVDIVX1 == RVDIVX2) {
			isTRUE = 1;
		} else {
			isTRUE = 0;
		}
		
		if (RVDIVX2 == RVDIVX3) {
			isTRUE2 = 1;
		} else {
			isTRUE2 = 0;
		}
		
		System.out.println(isTRUE);
		System.out.println(isTRUE2);
		
		// Identisch
		// OV1 in Gerade 2 einsetzen
		// OV2 von OV1 abziehen

		// SystemXn für LGS
		float SystemX1, SystemX2, SystemX3;
		SystemX1 = Punkt2X1-PunktX1;
		SystemX2 = Punkt2X2-PunktX1;
		SystemX3 = Punkt2X3-PunktX1;
		
		// Jetzt steht nur noch OV1 da; SystemXn = r*RV2
		// Gleichungssystem aufstellen und Lösungen checken
		
		
		
		
		
		
		//Else Gleichstellen
		
		
	}

}

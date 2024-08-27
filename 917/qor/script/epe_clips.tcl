# For removing any error, occured in first screenshot 
view bbox 0 0 400 400
view snapshot dummy.png 
view snapshot dummy.png 

 
 
#-----For EPE_Target_vs_Mask_Simulation_Negfocus has 200:23
# show EPE_Target_vs_Mask_Simulation_Negfocus 
# Delete all caddata
caddata delete * 
# Load in the target input oasis file 
caddata current target 
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_t/target_871.oas
palette dashed target 1:1 0 
palette stipple target 1:1 9 
palette edgecolor target 1:1 0 0 1 
# Load in the simulation input oasis file
caddata current simulation
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_s/simu_ndefocus_871.oas
palette dashed simulation 1:1 0 
palette stipple simulation 1:1 0 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001/mask_871.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/001/part_871.oas
palette fillcolor errors 200:23 1 0 1 
palette stipple errors 200:23 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:23 
palette stipple errors 200:23 8 
palette edgecolor errors 200:23 1 0 0 
palette dashed errors 200:23 0 

palette dashed mask 10:0 0
palette stipple mask 10:0 9
palette edgecolor mask 10:0 1 0 0
palette edgecolor mask 10:0 0.666667 0 0.498039
palette stipple mask 10:0 8
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0.498039
palette dashed target 10:0 0
palette stipple target 10:0 9
palette edgecolor target 10:0 0 0 1
palette fillcolor target 10:0 0 0 1
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 833198.500000 33097.500000 833598.500000 33497.500000 
view center 833398.500000 33297.500000 
marker create 833398.500000 33297.500000 
view snapshot /home/centos/11610/qor/asset/epenegfocuspc_200_23.png 

 
 
#-----For EPE_Target_vs_Mask_Simulation_Negdose has 200:21
# show EPE_Target_vs_Mask_Simulation_Negdose 
# Delete all caddata
caddata delete * 
# Load in the target input oasis file 
caddata current target 
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/004_t/target_694.oas
palette dashed target 1:1 0 
palette stipple target 1:1 9 
palette edgecolor target 1:1 0 0 1 
# Load in the simulation input oasis file
caddata current simulation
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/004_s/simu_ndose_694.oas
palette dashed simulation 1:1 0 
palette stipple simulation 1:1 0 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/004/mask_694.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/004/part_694.oas
palette fillcolor errors 200:21 1 0 1 
palette stipple errors 200:21 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:21 
palette stipple errors 200:21 8 
palette edgecolor errors 200:21 1 0 0 
palette dashed errors 200:21 0 

palette dashed mask 10:0 0
palette stipple mask 10:0 9
palette edgecolor mask 10:0 1 0 0
palette edgecolor mask 10:0 0.666667 0 0.498039
palette stipple mask 10:0 8
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0.498039
palette dashed target 10:0 0
palette stipple target 10:0 9
palette edgecolor target 10:0 0 0 1
palette fillcolor target 10:0 0 0 1
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 679994.800000 133142.900000 680394.800000 133542.900000 
view center 680194.800000 133342.900000 
marker create 680194.800000 133342.900000 
view snapshot /home/centos/11610/qor/asset/epenegdosepc_200_21.png 

 
 
#-----For EPE_Target_vs_Nominal_Mask_Simulation_f0d0 has 200:20
# show EPE_Target_vs_Nominal_Mask_Simulation_f0d0 
# Delete all caddata
caddata delete * 
# Load in the target input oasis file 
caddata current target 
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_t/target_871.oas
palette dashed target 1:1 0 
palette stipple target 1:1 9 
palette edgecolor target 1:1 0 0 1 
# Load in the simulation input oasis file
caddata current simulation
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_s/simu_871.oas
palette dashed simulation 1:1 0 
palette stipple simulation 1:1 0 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001/mask_871.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/001/part_871.oas
palette fillcolor errors 200:20 1 0 1 
palette stipple errors 200:20 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:20 
palette stipple errors 200:20 8 
palette edgecolor errors 200:20 1 0 0 
palette dashed errors 200:20 0 

palette dashed mask 10:0 0
palette stipple mask 10:0 9
palette edgecolor mask 10:0 1 0 0
palette edgecolor mask 10:0 0.666667 0 0.498039
palette stipple mask 10:0 8
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0.498039
palette dashed target 10:0 0
palette stipple target 10:0 9
palette edgecolor target 10:0 0 0 1
palette fillcolor target 10:0 0 0 1
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 833196.200000 33101.300000 833596.200000 33501.300000 
view center 833396.200000 33301.300000 
marker create 833396.200000 33301.300000 
view snapshot /home/centos/11610/qor/asset/epenompc_200_20.png 

 
 
#-----For EPE_Target_vs_Mask_Simulation_Posfocus has 200:24
# show EPE_Target_vs_Mask_Simulation_Posfocus 
# Delete all caddata
caddata delete * 
# Load in the target input oasis file 
caddata current target 
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_t/target_871.oas
palette dashed target 1:1 0 
palette stipple target 1:1 9 
palette edgecolor target 1:1 0 0 1 
# Load in the simulation input oasis file
caddata current simulation
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_s/simu_pdefocus_871.oas
palette dashed simulation 1:1 0 
palette stipple simulation 1:1 0 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001/mask_871.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/001/part_871.oas
palette fillcolor errors 200:24 1 0 1 
palette stipple errors 200:24 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:24 
palette stipple errors 200:24 8 
palette edgecolor errors 200:24 1 0 0 
palette dashed errors 200:24 0 

palette dashed mask 10:0 0
palette stipple mask 10:0 9
palette edgecolor mask 10:0 1 0 0
palette edgecolor mask 10:0 0.666667 0 0.498039
palette stipple mask 10:0 8
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0.498039
palette dashed target 10:0 0
palette stipple target 10:0 9
palette edgecolor target 10:0 0 0 1
palette fillcolor target 10:0 0 0 1
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 833198.500000 33097.500000 833598.500000 33497.500000 
view center 833398.500000 33297.500000 
marker create 833398.500000 33297.500000 
view snapshot /home/centos/11610/qor/asset/epeposfocuspc_200_24.png 

 
 
#-----For EPE_Target_vs_Mask_Simulation_Posdose has 200:22
# show EPE_Target_vs_Mask_Simulation_Posdose 
# Delete all caddata
caddata delete * 
# Load in the target input oasis file 
caddata current target 
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_t/target_871.oas
palette dashed target 1:1 0 
palette stipple target 1:1 9 
palette edgecolor target 1:1 0 0 1 
# Load in the simulation input oasis file
caddata current simulation
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001_s/simu_pdose_871.oas
palette dashed simulation 1:1 0 
palette stipple simulation 1:1 0 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/001/mask_871.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/001/part_871.oas
palette fillcolor errors 200:22 1 0 1 
palette stipple errors 200:22 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:22 
palette stipple errors 200:22 8 
palette edgecolor errors 200:22 1 0 0 
palette dashed errors 200:22 0 

palette dashed mask 10:0 0
palette stipple mask 10:0 9
palette edgecolor mask 10:0 1 0 0
palette edgecolor mask 10:0 0.666667 0 0.498039
palette stipple mask 10:0 8
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0.498039
palette dashed target 10:0 0
palette stipple target 10:0 9
palette edgecolor target 10:0 0 0 1
palette fillcolor target 10:0 0 0 1
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9
palette dashed simulation 10:0 0
palette edgecolor simulation 10:0 1 0 0
palette stipple simulation 10:0 9

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 833197.700000 33096.000000 833597.700000 33496.000000 
view center 833397.700000 33296.000000 
marker create 833397.700000 33296.000000 
view snapshot /home/centos/11610/qor/asset/epeposdosepc_200_22.png 

 
 
#-----For Width_of_PV_Band_by_Dose has 200:41
# show Width_of_PV_Band_by_Dose 
# Delete all caddata
caddata delete * 
# Load in the mask input oasis file
caddata current mask
import caddatasource /home/centos/11610/intermediate/fermi.output/contact_target/005/mask_665.oas
palette dashed mask 1:1 0 
palette stipple mask 1:1 0 
caddata current errors 
import caddatasource /home/centos/11610/intermediate/fermi.output/verification/005/part_665.oas
palette fillcolor errors 200:41 1 0 1 
palette stipple errors 200:41 8 
palette hide errors 200:0 
palette hide errors 200:1 
palette hide errors 200:2 
palette hide errors 200:3 
palette hide errors 200:4 
palette hide errors 200:10 
palette hide errors 200:11 
palette hide errors 200:12 
palette hide errors 200:13 
palette hide errors 200:14 
palette hide errors 200:20 
palette hide errors 200:21 
palette hide errors 200:22 
palette hide errors 200:23 
palette hide errors 200:24 
palette hide errors 200:31 
palette hide errors 200:32 
palette hide errors 200:41 
palette hide errors 200:42 
# Remove any previous markers 
marker clear * 
# turn on error marker 
palette show errors 200:41 
palette stipple errors 200:41 8 
palette edgecolor errors 200:41 1 0 1 
palette fillcolor errors 200:41 1 0 1 

palette dashed mask 10:0 0
palette edgecolor mask 10:0 0.666667 0 0
palette stipple mask 10:0 0
palette fillcolor mask 10:0 0.666667 0 0

# Zoom in to the error location and take snap shot. 
view bbox 0 0 0 0
view bbox 634802.500000 165132.700000 635202.500000 165532.700000 
view center 635002.500000 165332.700000 
marker create 635002.500000 165332.700000 
view snapshot /home/centos/11610/qor/asset/pvwidth_dose_200_41.png 
exit 

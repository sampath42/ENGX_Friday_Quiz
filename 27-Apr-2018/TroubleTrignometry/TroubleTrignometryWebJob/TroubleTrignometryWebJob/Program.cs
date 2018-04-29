using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.WebJobs;

namespace TroubleTrignometryWebJob
{
    // To learn more about Microsoft Azure WebJobs SDK, please see https://go.microsoft.com/fwlink/?LinkID=320976
    class Program
    {
        // Please set the following connection strings in app.config for this WebJob to run:
        // AzureWebJobsDashboard and AzureWebJobsStorage
        static void Main()
        {
            //var config = new JobHostConfiguration();
            
            //if (config.IsDevelopment)
            //{
            //    config.UseDevelopmentSettings();
            //}

            //var host = new JobHost(config);
            //// The following code ensures that the WebJob will be running continuously
            //host.RunAndBlock();

            TroubleTrignometryMethod();
        }

        private static string TroubleTrignometryMethod()
        {
            long[] inputs = { 3, 10, 2920383 };
            List<string> result = new List<string>();
            foreach (var input in inputs)
            {
                if (input >= 3 && input <= 3000000) // Constraint 3 <= n <= 3*10^6
                {
                    List<double> values = new List<double>();
                    for (int x = 0; x <= input; x++)
                    {
                        for (int y = 0; y <= input; y++)
                        {
                            for (int z = 0; z <= input; z++)
                            {
                                if ((x + y + z) == input)
                                {
                                    var res = Math.Sin(x) + Math.Sin(y) + Math.Sin(z);
                                    values.Add(res);
                                }
                            }
                        }
                    }
                    var max_result = values.Max();
                    var resultoutput = $"{input} -> {max_result}";
                    var round_max_result = Math.Round(max_result, 9);
                    var round_resultoutput = $"{input} -> {round_max_result}";
                    result.Add(resultoutput);
                    Console.WriteLine($"{resultoutput} , Decimals 9 = {round_resultoutput}");
                }
            }
            var resultStr = string.Join(",", result.ToArray());
            Console.WriteLine(resultStr);
            return resultStr;
        }
    }
}

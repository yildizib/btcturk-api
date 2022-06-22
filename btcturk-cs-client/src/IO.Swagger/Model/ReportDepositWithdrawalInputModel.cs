/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// ReportDepositWithdrawalInputModel
    /// </summary>
    [DataContract]
        public partial class ReportDepositWithdrawalInputModel :  IEquatable<ReportDepositWithdrawalInputModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ReportDepositWithdrawalInputModel" /> class.
        /// </summary>
        /// <param name="types">types.</param>
        /// <param name="currencies">currencies.</param>
        /// <param name="beginDate">beginDate.</param>
        /// <param name="endDate">endDate.</param>
        /// <param name="documentFileType">documentFileType.</param>
        public ReportDepositWithdrawalInputModel(List<int?> types = default(List<int?>), List<int?> currencies = default(List<int?>), DateTime? beginDate = default(DateTime?), DateTime? endDate = default(DateTime?), DocumentFileType documentFileType = default(DocumentFileType))
        {
            this.Types = types;
            this.Currencies = currencies;
            this.BeginDate = beginDate;
            this.EndDate = endDate;
            this.DocumentFileType = documentFileType;
        }
        
        /// <summary>
        /// Gets or Sets Types
        /// </summary>
        [DataMember(Name="types", EmitDefaultValue=false)]
        public List<int?> Types { get; set; }

        /// <summary>
        /// Gets or Sets Currencies
        /// </summary>
        [DataMember(Name="currencies", EmitDefaultValue=false)]
        public List<int?> Currencies { get; set; }

        /// <summary>
        /// Gets or Sets BeginDate
        /// </summary>
        [DataMember(Name="beginDate", EmitDefaultValue=false)]
        public DateTime? BeginDate { get; set; }

        /// <summary>
        /// Gets or Sets EndDate
        /// </summary>
        [DataMember(Name="endDate", EmitDefaultValue=false)]
        public DateTime? EndDate { get; set; }

        /// <summary>
        /// Gets or Sets DocumentFileType
        /// </summary>
        [DataMember(Name="documentFileType", EmitDefaultValue=false)]
        public DocumentFileType DocumentFileType { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class ReportDepositWithdrawalInputModel {\n");
            sb.Append("  Types: ").Append(Types).Append("\n");
            sb.Append("  Currencies: ").Append(Currencies).Append("\n");
            sb.Append("  BeginDate: ").Append(BeginDate).Append("\n");
            sb.Append("  EndDate: ").Append(EndDate).Append("\n");
            sb.Append("  DocumentFileType: ").Append(DocumentFileType).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as ReportDepositWithdrawalInputModel);
        }

        /// <summary>
        /// Returns true if ReportDepositWithdrawalInputModel instances are equal
        /// </summary>
        /// <param name="input">Instance of ReportDepositWithdrawalInputModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(ReportDepositWithdrawalInputModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Types == input.Types ||
                    this.Types != null &&
                    input.Types != null &&
                    this.Types.SequenceEqual(input.Types)
                ) && 
                (
                    this.Currencies == input.Currencies ||
                    this.Currencies != null &&
                    input.Currencies != null &&
                    this.Currencies.SequenceEqual(input.Currencies)
                ) && 
                (
                    this.BeginDate == input.BeginDate ||
                    (this.BeginDate != null &&
                    this.BeginDate.Equals(input.BeginDate))
                ) && 
                (
                    this.EndDate == input.EndDate ||
                    (this.EndDate != null &&
                    this.EndDate.Equals(input.EndDate))
                ) && 
                (
                    this.DocumentFileType == input.DocumentFileType ||
                    (this.DocumentFileType != null &&
                    this.DocumentFileType.Equals(input.DocumentFileType))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Types != null)
                    hashCode = hashCode * 59 + this.Types.GetHashCode();
                if (this.Currencies != null)
                    hashCode = hashCode * 59 + this.Currencies.GetHashCode();
                if (this.BeginDate != null)
                    hashCode = hashCode * 59 + this.BeginDate.GetHashCode();
                if (this.EndDate != null)
                    hashCode = hashCode * 59 + this.EndDate.GetHashCode();
                if (this.DocumentFileType != null)
                    hashCode = hashCode * 59 + this.DocumentFileType.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
